# -*- coding: utf-8 -*-
import scrapy

#导入数据模型
from zhilian.items import ZhilianItem
class Zl1Spider(scrapy.Spider):

    #爬虫名字要和文件名字相同
    name = 'zl2'
    #allowed_domains和start_urls一定要一样不然scrapy.Request无效
    allowed_domains = ['dangdang.com']
    #智联是动态页面，这里先用当当网的页面
    # start_urls = ['http://sou.zhaopin.com/?p=3&jl=530&sf=0&st=0&kw=java&kt=3']
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    def parse(self, response):
        #----------主页数据操作-----------------------
        print('url=',self.start_urls)
        titles = response.xpath('//a[@name="itemlist-title"]/@title').extract()
        prices = response.xpath('//span[@class ="price_n"]/text()').extract()
        list = []
        for i in range(0, len(titles)):
            map = {}
            map['title'] = titles[i]
            map['price'] = prices[i]
            list.append(map)

        print('list=', len(list))
        print('当前请求地址', response.request.url);
        print('获取上一次请求传递的数据meta=',response.meta)
        #获取页面
        # print('本页面=',response.body_as_unicode())
        str_url = response.request.url
        str_url = str_url[str_url.index('com/') + 4:str_url.index('-')]
        print('截取地址 str1=', str_url)

        zlitem=ZhilianItem()
        #禁止这样写 不然yield不起作用
        # zlitem.list=list
        zlitem['list']=list
        #每一页都存一个json
        zlitem['page']=str_url+'_data.json'
        zlitem['type'] = '主页'

        #保存主页数据
        # yield把数据给引擎在扔给pipelines.py的item
        #yield只是把任务加入队列
        yield zlitem
        # ------获取第一个子页面，子页面太多这里只做2个--------
        a_list=response.xpath('//a[contains(@name,"itemlist-picture") and contains(@target,"_blank") and contains(@class,"pic") and contains(@dd_name,"单品图片")]/@href').getall()
        print('子页面连接=',len(a_list))
        a_list=a_list[0:2]
        for i in range(0,len(a_list)):
            yield scrapy.Request(url=a_list[i], callback=self.childPage,meta={'info':'子页面','url':a_list[i]})

        print('子连接=',a_list)
        #------下一页--------
        # <a href="/pg3-cid4008154.html" title="下一页">下一页</a>
        #get()=/pg3-cid4008154.html
        url_str = response.xpath('//a[@title="下一页"]/@href').get()
        next_url = 'http://category.dangdang.com' + url_str
        print('next_url=',next_url)

        if  not url_str:
            # 退出方法
            return
        else:
            # 在把请求放到队列里面
            # callback=self.parse 解析的是同一个页面所以还用parse当前方法
            # allowed_domains和start_urls一定要一样不然scrapy.Request无效
            yield scrapy.Request(url=next_url, callback=self.parse,meta={'info':'数据','name':'李四','jsonName':str_url+'子页面'})


    #==================获取子页面======================================
    def childPage(self,response):
        print('------进入子页面------')
        list=response.xpath('//div[@class="name_info"]/h1/text()').get()
        print('子页面=',list)
        print('子页面meta=', response.meta)
        zlitem = ZhilianItem()
        zlitem['type']='子页面'
        zlitem['list']=list
        zlitem['page']='1.json'
        yield  list
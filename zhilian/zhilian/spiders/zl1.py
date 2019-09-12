# -*- coding: utf-8 -*-
import scrapy

#导入数据模型
from zhilian.items import ZhilianItem

class Zl1Spider(scrapy.Spider):
    name = 'zl1'
    allowed_domains = ['zhaopin.com']
    #智联是动态页面，这里先用当当网的页面
    # start_urls = ['http://sou.zhaopin.com/?p=3&jl=530&sf=0&st=0&kw=java&kt=3']
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    def parse(self, response):
        titles = response.xpath('//a[@name="itemlist-title"]/@title').extract()
        prices = response.xpath('//span[@class ="price_n"]/text()').extract()
        list = []
        for i in range(0, len(titles)):
            map = {}
            map['title'] = titles[i]
            map['price'] = prices[i]
            list.append(map)

        print('list=', len(list))

        zlitem=ZhilianItem()
        #禁止这样写 不然yield不起作用
        # zlitem.list=list
        zlitem['price']=prices
        zlitem['title']=titles
        zlitem['list']=list
        zlitem['data']=list
        # yield把数据给引擎在扔给pipelines.py的item
        yield zlitem

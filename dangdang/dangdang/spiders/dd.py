# -*- coding: utf-8 -*-
import scrapy
#所有的导入都是从核心目录中导入
#核心目录是“dangdang”
from dangdang.items import DangdangItem

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    #第一页的连接http://category.dangdang.com/pg1-cid4008154.html
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    #scrapy会自动爬取，都存到response里面
    def parse(self, response):
        dd_item=DangdangItem()

        #title属性值
        dd_item['title']=response.xpath('//a[@name="itemlist-title"]/@title').extract()
        #href值
        dd_item['link'] = response.xpath('//a[@name="itemlist-title"]/@href').extract()
        #提取评论数
        dd_item['comment'] = response.xpath('//a[@dd_name = "单品评论"]/text()').extract()
        #输出
        # print('dd_item=', dd_item)
        # print('title',dd_item['title'],'link=',dd_item['link'],'comment=',dd_item['comment'])
        #把dd_item数据提交到pipelines.py中
        yield dd_item
        # pass











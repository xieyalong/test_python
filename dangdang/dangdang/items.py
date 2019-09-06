# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #获取标题
    title=scrapy.Field()
    #获取连接
    link=scrapy.Field()
    #评论
    comment=scrapy.Field()





















# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#定义数据模型
#也可以不用直接zl1.py以map的方式yield给pipelines.py
#好处就是想要什么字段很明确，显着专业一点
#这时的pipelines.py里面的item数据类型就是ZhilianItem，而不是map了
class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field()
    list=scrapy.Field()
    data=scrapy.Field()

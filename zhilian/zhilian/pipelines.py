# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import  json
#运行轨迹 open_spider->zl1.pay->process_item->close_spider
class ZhilianPipeline(object):

    # 开始 self：代表this
    def open_spider(self,spider):
        #给对象创建变量
        self.abc='开始爬虫'
        print(self.abc)

    def process_item(self, item, spider):
        print('item=',item['list'])
        #存入文件
        with open('data.json','w',encoding='utf-8') as fw:
            fw.write(json.dumps(item['list'],ensure_ascii=False))
        return item

    def close_spider(self,spider):
        self.abc = '结束爬虫'
        print(self.abc)
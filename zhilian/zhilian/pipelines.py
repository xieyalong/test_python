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
        print('item=',len(item['list']),'page=',item['page'],'type=',item['type'])
        #以追加的方式网文件内写入
        if '主页'==item['type']:
            with open(item['page'],'a',encoding='utf-8') as fw:
                fw.write(json.dumps(item['list'],ensure_ascii=False))
        elif '子页'==item['type']:
            with open(item['page'], 'a', encoding='utf-8') as fw:
                fw.write(json.dumps(item['list'], ensure_ascii=False))

        return item

    def close_spider(self,spider):
        self.abc = '结束爬虫'
        print(self.abc)
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DangdangPipeline(object):
    #item就是dd.py里面的dd_item
    #dd_item=['title':[],'link':[],'comment':[]]
    def process_item(self, item, spider):
        print('-----pipelines.py开始--------------')
        #处理title数据
        titles=item['title']
        links=item['link']
        comments=item['comment']
        size=len(titles)
        list=[]
        for i in range(0,size):
            map={}
            map['title']=titles[i]
            map['link']=links[i]
            map['comment']=comments[i]
            list.append(map)
            # print('title=',title,'link=',link,'comment=',comment)
        print('list=',list)
        with open('dd.json','w',encoding='utf-8')  as fw:
            fw.write(json.dumps(list,ensure_ascii=False))
        print('-----pipelines.py结束--------------')
        return item

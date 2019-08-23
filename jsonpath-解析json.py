

import  json
import jsonpath

#获取文件json数据
def getData():
    with open('jsonpath测试数据.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
        return data;

#转成python对象
jsondata=getData()
# print(data['store']['book'][0])
#====================
#"$"：根元素
#“.”或者“[]”：子元素
#"*":通配符
#“..”：内容级
#====================
#查找book下的所有的title
str=jsonpath.jsonpath(jsondata,'$.store.book[*].title')
print('查找book下的所有的title=',str)
#查找第1个title
str=jsonpath.jsonpath(jsondata,'$.store.book[0].title')
print('查找第1个title=',str)
#找到根目录下的所有title
str=jsonpath.jsonpath(jsondata,'$..title')
print('找到根目录下的所有title=',str)

#查找bicycle下的所有元素
str=jsonpath.jsonpath(jsondata,'$..bicycle.*')
print('“..”和“*”查找，查找bicycle下的所有元素=',str)

str=jsonpath.jsonpath(jsondata,'$.store.*')
print('“..”查找，查找根木目录下store下的所有元素=',str)

str=jsonpath.jsonpath(jsondata,'$..book[0]')
print('“..”查找，获取book下0索引=',str)

str=jsonpath.jsonpath(jsondata,'$..book[(@.length-1)]')
print('查找book当前目录下的最后1个=',str)

str=jsonpath.jsonpath(jsondata,'$..book[0,1]')
print('查找前2本书=',len(str))

str=jsonpath.jsonpath(jsondata,'$..book[:2]')
print('截取前2本书=',len(str))

str=jsonpath.jsonpath(jsondata,'$..book[?(@.isbn)]')
print('查找book下有isbn字段的json=',len(str))

str=jsonpath.jsonpath(jsondata,'$..book[?(@.price<10)]')
print('查找book下低于10块钱的书=',str)








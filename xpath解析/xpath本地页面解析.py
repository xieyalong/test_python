
#导包
from lxml import etree

#直接写parse()会报错，毕竟不是xml
# html=etree.parse('1.html')
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse(r'html\xpath本地纯网页.html', parser=parser)
print(html)

list=html.xpath('//span')
print('当前节点下所有span,各个层级=',len(list))

list=html.xpath('//span[@class="p2 p3"]')
print('当前节点下class="p2 p3"所有span=',len(list))

#只获取text内容，span里面有子节点不会获取
list=html.xpath('//span[@class="p2 p3"]/text()');
print('class="p2 p3"所有span的内容=',list)

list=html.xpath('//a[@id="_id"]/@href')
print('根据一个属性获取href值=',list)

list=html.xpath('//a[contains(@title,"赵匡胤") and contains(@id,"_id") and contains(@about,"_about")]/@href')
print('根据多个属性获取href值=',list)

list=html.xpath('//div[@id="_div3"]/span/text()')
print('获取div子元素span的内容=',list)

#p标签不起作用，如果换做span就起作用
list=html.xpath('//p[@class="p1"]/div/text()')
print('====',list)

# with open(r'aaaa.html','w',encoding='utf-8') as fw:
#     fw.write(str(html))





















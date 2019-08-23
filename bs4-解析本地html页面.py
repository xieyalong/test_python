
#bs4=标签解析
from bs4 import BeautifulSoup

#bs4-本地纯网页.html 和本文件同级目录
#bs=整个html页面
#bs = BeautifulSoup("网络获取的网页内容", 'lxml')
#open('本地的网页',编码格式)
bs =BeautifulSoup(open('bs4-本地纯网页.html',encoding='UTF-8'),'lxml')
#输出整个页面
# # print(sb)

#=====================
#find和bs.div都是找的符合要求的第一个,
#返回：标签对象

#-----根据标签名查找--------
#标签名查找特性：只能找到第一个符合要求的标签
#在bs.的时候不会有标签的提示，直接写上去就行

#查找a标签 只能获取第一个
print('a标签=',bs.a)
#查找div标签 只能获取第一个
print('div标签',bs.div)
print('----------------------')
#-----获取标签属性值--------
#bs.a.attr特性：获取所有属性，返回字典
#如 a标签设置了id，href属性，只能获取这两个属性


print('获取a标签已经写上的属性=',bs.a.attrs)
print('获取a标签的href值,使用attrs["href"]属性=',bs.a.attrs['href'])
print('获取a标签的href值=',bs.a['href'])
print('获取a标签的title值=',bs.a['title'])
print('----------------------')
#-----获取标签内容-------
#特性：text和get_text()标签里面有标签和文字，
#只会把标签顾虑掉，换行不会过滤
print('获取a标签内容=',bs.div.text)
print('获取a标签内容=',bs.div.get_text())
#特性：标签里面只是文字，没有标签才能获取
print('获取a标签内容=',bs.div.string)
print('----------------------')
#-----find查询---------
# find特性：等价于bs.a;bs.find('a')==bs.a，只能获取第一个标签

print('a标签=',bs.find('a'))
print('根据href属性过滤=',bs.find('a',href='http://www.163.com'))
print('根据id属性过滤=',bs.find('p',id='xiaoHe'))
#class 是关键字必须是“class_”
print('根据class属性过滤=',bs.find('p',class_='hanCss'))
print('根据class属性过滤,获取里面的内容=',bs.find('p',class_='hanCss').text)
print('----------------------')
#-----find子级查询---------
div=bs.find('div',class_='tang')
a=div.find('a',id='als')
print('a标签内容=',a.text,'a标签href=',a['href'])
print('----------------------')
#=============================
#find_all查询
#特性：把所有符合的标签都查出来
#返回:有1个返回的是标签对象，有多个返回的是list
#-----find_all查询---------
list=bs.find_all('a')
print('查询所有的a标签=',len(list))
list=bs.find_all('a',id='als')
print('查询所有a标签id=als',len(list))
#返回list
list=bs.find_all(['span','img'])
print('同时查询多个标签=',len(list))
list=bs.find_all('p',limit=2)
print('查找p标签取前两个=',list)
print('----------------------')
#===========================
# select 选择器()，返回list，里面有1个也是list,必须有下标获取
#标签选择器（div），类选择器(.xyl,class=xyl)，id选择器(#xyl,id=xyl)，
# 组合选择器(div,.xyl,#xyl),
#层级选择器（内容级或者多级，不分子和孙子：div .xyl #xyl下的标签，只要满足子级就符合；）
# （下一级：div>p>.xyl>#xyl），
# 伪类选择器（），属性选择器（input[name='xyl']）
#--------------------
list=bs.select('span')
print('标签选择器=',len(list))
list=bs.select('#als')
print('id选择器=',list[0])
list=bs.select('.hanCss')
print('类选择器=',list)
list=bs.select('#xiaoHe,.hanCss')
print('组合选择器1=',list)
list=bs.select('.c1,.c2')
print('组合选择器2=class="c1 c2"的标签，必须2个同事满足',len(list))
list=bs.select('.tang>ul>#lispan>span')
print('层级选择器 查找class=tang下ul标签下id=lispan下的span标签=',list)
list=bs.select('input[value="1"],[alt="_i"]')
print('属性选择器1=',list)
list=bs.select('input[name="_i2"],[name="_i3"]')
print('属性选择器2=',list)

print('----------------------')
#===========================
#结合使用
list=bs.find_all('div',class_='song')
for html in list:
    for html2 in html.select('.xyl'):
         print(html2.text)





































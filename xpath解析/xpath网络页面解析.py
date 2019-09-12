
import  time
from selenium import webdriver
from lxml import etree


#==========================
# 模拟手动 进入智联-》点击弹出框
#----------------------------
#驱动路径：
path=r'C:\pythonWorkspace\chromedriver.exe'

#创建谷歌浏览器，通过对象操作浏览器
#webdriver.Chrome():使用的是谷歌的浏览器
#运行就会打开浏览器，模拟手点击了桌面上的谷歌浏览器
browser= webdriver.Chrome(executable_path=path)
print('浏览器对象',browser)
#智联
url='https://sou.zhaopin.com/?p=3&jl=530&sf=0&st=0&kw=java&kt=3'
#打开智联
browser.get(url)
time.sleep(2)


#根据class查找；找到提示弹出框
div_dialog=browser.find_element_by_class_name('risk-warning__content')
time.sleep(2)

#子级查询，根据标签名称查找;找到弹出框下的button,点击“知道了”
button=div_dialog.find_element_by_tag_name('button')
button.click()

# print('获取整个页面=',browser.page_source)
#解析网络页面
parser = etree.HTMLParser(encoding='utf-8')
html=etree.HTML(browser.page_source,parser=parser)
#解析本地
# html=etree.parse(browser.page_source,parser=parser)

list=html.xpath('//title/text()')
print('title标签的内容=',list)
list=html.xpath('//a[@class="contentpile__content__wrapper__item__info__box__cname__title company_title"]/text()')
print('公司名称=',len(list),list)

print('------结束----')
html=browser.find_elements_by_class_name('contentpile__content__wrapper__item__info__box__jobname__title')
print('根据class属性值查找=',len(html))
browser.quit()






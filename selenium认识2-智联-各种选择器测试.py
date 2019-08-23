

import  time
#导入包
from selenium import webdriver
#==========================
# 模拟手动 打开谷歌->输入www.baidu.com->搜索“谢亚龙”->点击“百度一下”
#----------------------------
#驱动路径：
path=r'C:\pythonWorkspace\chromedriver.exe'

#创建谷歌浏览器，通过对象操作浏览器
#webdriver.Chrome():使用的是谷歌的浏览器
#运行就会打开浏览器，模拟手点击了桌面上的谷歌浏览器
browser= webdriver.Chrome(executable_path=path)
print('浏览器对象',browser)

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
print('根据子级button标签查找')

#查看所有的title
html=browser.find_elements_by_class_name('contentpile__content__wrapper__item__info__box__jobname__title')
print('根据class属性值查找=',len(html))

html=browser.find_elements_by_link_text('北京得网时代信息技术有限公司')
print('根据a标签的内容查找=',len(html))

html=browser.find_elements_by_name('loginname')
print('根据name属性值查找=',len(html))

#可能说明是同一个标签
html=browser.find_elements_by_css_selector('img[align="absmiddle"][alt="看不清？点击更换"]')
print('属性选择器查找1=',len(html))

#有“,”说明是查找所有div的标签class=layer__topbar||class=zp-searchs
html=browser.find_elements_by_css_selector('div[class="layer__topbar"],[class="zp-searchs"]')
print('组合属性选择器查找2=',len(html))

html=browser.find_element_by_id('search')
print('id选择器查找=',html)

html=browser.find_elements_by_css_selector('.souheader__channel__item__name,#search')
print('组合选择器查找=',len(html))

html=browser.find_elements_by_css_selector('.souheader>ul>.souheader__channel__item')
print('层级选择器选择器查找=',len(html))


#关闭(关闭)浏览器,
browser.quit()




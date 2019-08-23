

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

url='http://www.baidu.com/'
#打开百度
browser.get(url);
#停留3秒，模拟真人操作 如果立马找浏览器还没有加载完肯定找不到
time.sleep(3)
#查找input输入框
my_input=browser.find_element_by_id('kw')
print('input=',my_input)
#设置input的内容，输入关键字，查找“谢亚龙”
my_input.send_keys('谢亚龙')
time.sleep(3)
#查找搜索按钮“百度一下”
my_button=browser.find_element_by_id('su')
#触发“百度一下”的单击事件
my_button.click()
time.sleep(3)
my_a=browser.find_element_by_link_text('谢亚龙_百度百科')
print(my_a)
my_a.click()
time.sleep(10)
#关闭(关闭)浏览器,
browser.quit()


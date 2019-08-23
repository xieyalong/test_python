

import  time
#导入包
from selenium import webdriver

#驱动路径：
path=r'C:\pythonWorkspace\chromedriver.exe'

#创建谷歌浏览器，通过对象操作浏览器
#webdriver.Chrome():使用的是谷歌的浏览器
browser= webdriver.Chrome(executable_path=path)
#打开浏览器，print就是把谷歌浏览器打开了,模拟的是手动点击了桌面上的谷歌浏览器
print(browser)

url='http://www.baidu.com/'
#浏览百度
browser.get(url);
#停留5秒
time.sleep(2)
#关闭(关闭)浏览器,
browser.quit()


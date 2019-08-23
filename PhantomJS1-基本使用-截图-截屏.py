

from  selenium import  webdriver
import  time

path=r'C:\pythonWorkspace\phantomjs.exe'
#创建浏览器对象
browser=webdriver.PhantomJS(path)
url='http://www.baidu.com/'
#浏览百度
browser.get(url)
time.sleep(2)
#因无页面操作，可以截图查看，保存到本目录下,phantomjs2
browser.save_screenshot(r'phantomjs\baidu2.png')
#关键字
my_input=browser.find_element_by_id('kw')
my_input.send_keys('谢亚龙')
browser.save_screenshot(r'phantomjs\guanjianzi.png')
time.sleep(2)
#点击“百度一下”
my_button=browser.find_element_by_id('su')
my_button.click()
browser.save_screenshot(r'phantomjs\baiduyixia.png')
time.sleep(3)
#点击“谢亚龙_百度百科”
my_a=browser.find_element_by_link_text('谢亚龙_百度百科')
my_a.click()
time.sleep(10)
browser.save_screenshot(r'phantomjs\baidubaike.png')

print('----结束----')
time.sleep(10)
browser.quit()









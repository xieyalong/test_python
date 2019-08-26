

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import  time

#无界面模式
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path=r'C:\pythonWorkspace\chromedriver.exe'
browser= webdriver.Chrome(executable_path=path,options=chrome_options)
# browser= webdriver.Chrome(executable_path=path)
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
#查找百度百科,跳转到百度百科
page=browser.find_elements_by_css_selector('.t.c-gap-bottom-small')[0]
print(page.text)
my_a=page.find_element_by_tag_name('a')
my_a.click()
print(my_a.text)
time.sleep(10)
browser.save_screenshot('谷歌无界面浏览器\百度百科.png')

#关闭(关闭)浏览器,
browser.quit()
print('结束')



# url='https://www.baidu.com/'
# #打开浏览器
# browser.get(url)
# browser.save_screenshot('谷歌无界面浏览器\谷歌无界面浏览器拍照.png')
#
# time.sleep(3)
# browser.quit()




from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import  time

#无界面模式
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path=r'C:\pythonWorkspace\chromedriver.exe'
browser= webdriver.Chrome(executable_path=path,options=chrome_options)
#有页面
# browser= webdriver.Chrome(executable_path=path)
url='http://www.baidu.com/'
#打开百度
browser.get(url);
#停留3秒，模拟真人操作 如果立马找浏览器还没有加载完肯定找不到
time.sleep(30)
browser.save_screenshot()

# time.sleep(3)
# browser.quit()
print('结束')


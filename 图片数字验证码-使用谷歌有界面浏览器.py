

from  selenium import  webdriver
import  time
from bs4 import BeautifulSoup
import  json

path=r'C:\pythonWorkspace\chromedriver.exe'
browser= webdriver.Chrome(executable_path=path)
url='https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
browser.get(url=url)
time.sleep(3)
with open(r'文件\登录古文诗词网.html','w',encoding='utf-8') as f:
    f.write(browser.page_source)
#账号
email=browser.find_element_by_id('email')
email.send_keys('17744488225')
time.sleep(2)
# 密码
email=browser.find_element_by_id('pwd')
email.send_keys('a123456')
time.sleep(2)
#等待手动输入
codev=input('请输入验证码')
time.sleep(2)
#验证码
code=browser.find_element_by_id('code')
code.send_keys(codev)
time.sleep(3)
#登录
denglu=browser.find_element_by_id('denglu')
denglu.click()
time.sleep(2)
print('结束')
# time.sleep(30)
# browser.quit()
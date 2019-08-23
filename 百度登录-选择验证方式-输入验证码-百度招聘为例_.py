

from  selenium import  webdriver
import  time
from bs4 import BeautifulSoup
import  json

# path=r'C:\pythonWorkspace\phantomjs.exe'
path=r'C:\pythonWorkspace\chromedriver.exe'
#创建浏览器对象
# browser=webdriver.PhantomJS(path)
browser= webdriver.Chrome(executable_path=path)
url='https://zhaopin.baidu.com/quanzhi?query=%E7%99%BE%E5%BA%A6%E6%8B%9B%E8%81%98&city_sug=%E5%8C%97%E4%BA%AC&zp_fr=aladdin-5463-zp_exact_new'
browser.get(url=url)
time.sleep(3)
#选择账号登录
objElement=browser.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn')
objElement.click()
time.sleep(3)
#账号
objElement=browser.find_element_by_id('TANGRAM__PSP_3__userName')
objElement.send_keys('535030765@qq.com')
objElement.click()
time.sleep(2)
#密码
objElement=browser.find_element_by_id('TANGRAM__PSP_3__password')
objElement.send_keys('密码')
objElement.click()
time.sleep(2)
#登录
objElement=browser.find_element_by_id('TANGRAM__PSP_3__submit')
objElement.click()
time.sleep(2)

#这里家try except 因为百度验证过的就不在验证了，第二次启动这步缺少会报错
try:
     # 选择验证方式
     objElement = browser.find_element_by_id('TANGRAM__22__select_show_arrow')
     objElement.click()
     time.sleep(2)
     # 选择邮箱
     objElement = browser.find_element_by_id('TANGRAM__22__select_email')
     objElement.click()
     time.sleep(2)

     # 发送邮箱验证码
     objElement = browser.find_element_by_id('TANGRAM__22__button_send_email')
     objElement.click()
     time.sleep(2)

     # 输入验证啊 这里最好是通过子线程，如果发现里面有数据了就读取出来
     code = ''
     # with open('C:\code\code.text','r',encoding='utf-8') as fr:
     #      code=fr.read()
     # 这里使用输入方法
     code = input("请输入百度验证码")
     print(code)
     objElement = browser.find_element_by_id('TANGRAM__22__input_label_vcode')
     objElement.send_keys(code)
     time.sleep(2)
     # 点击确定
     objElement = browser.find_element_by_id('TANGRAM__22__button_submit')
     objElement.click()
     time.sleep(2)
except Exception as e:
     print(e)

#开始进入招聘页面
print('开始进入招聘页面')


# browser.quit()
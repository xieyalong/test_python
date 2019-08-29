

import  time
#导入包
from selenium import webdriver


path=r'C:\pythonWorkspace\chromedriver.exe'
browser= webdriver.Chrome(executable_path=path)
browser.get('https://so.gushiwen.org/shiwen/')

time.sleep(2)
a=browser.find_element_by_css_selector('a[target="_blank"][style="font-size:18px; line-height:22px; height:22px;"]')
print(a.text)
print('跳转前 页面=',browser.window_handles,'--size=',len(browser.window_handles),'--当前页面1=',browser.current_window_handle)
a.click()
time.sleep(2)
#获取下一个页面索引
window_index=len(browser.window_handles)-1
#跳转下一个页面
browser.switch_to.window(browser.window_handles[window_index])
print('跳转后 页面=',browser.window_handles,'--size=',len(browser.window_handles),'--当前页面1=',browser.current_window_handle,'--当前页面2=',browser.window_handles[1])
#保存子页面的源码
with open(r'文件\1.html','w',encoding='utf-8') as f:
    f.write(browser.page_source)







import requests
#导入浏览器包
from selenium import webdriver
import  time
import  json


#浏览器驱动路径
browser_path=r'C:\pythonWorkspace\chromedriver.exe'
#创建浏览器对象
browser= webdriver.Chrome(executable_path=browser_path)
#打开浏览器兵进入365yg的页面
browser.get('https://www.365yg.com')

time.sleep(3)
html_src_list=browser.find_element_by_css_selector('a[target="_blank"][class="img-wrap"]')
# print('视频数量=',len(html_src_list))
time.sleep(2)
print('页面1=',browser.current_window_handle,'--list=',browser.window_handles)
html_src_list.click()
time.sleep(3)
#获取下一个页面索引
window_index=len(browser.window_handles)-1
#跳转下一个页面
browser.switch_to.window(browser.window_handles[window_index])
print('页面2=',browser.current_window_handle,'--list=',browser.window_handles)
time.sleep(3)
#点击播放播视频
start=browser.find_element_by_class_name('xgplayer-start')
start.click()
time.sleep(3)

print(browser.get_network_conditions())

browser.get_network_conditions()


# with open(r'文件\start.html','w',encoding='utf-8') as f:
#     f.write(browser.page_source)
# time.sleep(2)



# video=browser.find_element_by_tag_name('video')
# print(video.get_attribute('src'))



# video=browser.find_element_by_tag_name('video')
# print(video.get_attribute('src'))

print('结束')




# for v in html_src_list:
#     img=v.find_element_by_class_name('lazy-load-img')
#     a=v.find_element_by_css_selector('a[target="_blank"][class="link"]')
#     print('src=',img.get_attribute('src'),'title=',a.text)

# html_src_list=browser.find_elements_by_css_selector('a[target="_blank"][class="link"]')
# print('title数量=',len(html_src_list))
# for v in html_src_list:
#     print(v.text,v.get_attribute('href'))




#退出
# time.sleep(30)
# browser.quit()







# #视频地址
# url='http://v3-default.ixigua.com/737d3fe768d56ad62b1dcdd38876444d/5d6780d7/video/m/2209d5be05ddb7341f49f791a60abef90511162bf1bc00003c348645cee5/?rc=Mzk1a3huOmtkbjMzNzczM0ApdSk3NTY0Nzg0NDw6Nzw7PDNAKWVoZDNpZzllZTdmN2Y8ZWlnKXUpQGczdSlAZjN1KTk0ZF9xLWljLW82YV8tLTEtMHNzOmkyNTAxMS0yLS0vLy4vLS4vaV8uXmE0Ly9eYjYzYGE2NS86YzpiMHAjOmEtcCM6YDU0Og%3D%3D'
# #伪装头部
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# #请求
# r=requests.get(url=url,headers=headers)
#
# #写入文件
# with open(r'视频\1.mp4','wb') as f:
#     #r.content：二进制写入
#     f.write(r.content)
#
# print('处理完成')




# http://v3-default.ixigua.com/737d3fe768d56ad62b1dcdd38876444d/5d6780d7/video/m/2209d5be05ddb7341f49f791a60abef90511162bf1bc00003c348645cee5/?rc=Mzk1a3huOmtkbjMzNzczM0ApdSk3NTY0Nzg0NDw6Nzw7PDNAKWVoZDNpZzllZTdmN2Y8ZWlnKXUpQGczdSlAZjN1KTk0ZF9xLWljLW82YV8tLTEtMHNzOmkyNTAxMS0yLS0vLy4vLS4vaV8uXmE0Ly9eYjYzYGE2NS86YzpiMHAjOmEtcCM6YDU0Og%3D%3D





# <a href="/group/6730132245517976078/" target="_blank" class="link">好心让座竟然被打 以怨报德终究付出代价</a>








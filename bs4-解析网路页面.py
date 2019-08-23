
import  urllib.request
import urllib.parse
from bs4 import  BeautifulSoup
import  time
#================================================
page_index=0
page_size=2
#搜索java职位
kw='java'
#https://sou.zhaopin.com/?p=3&jl=530&kw=java&kt=3&sf=0&st=0
#%E9%83%91%E5%B7%9E=郑州
#https://sou.zhaopin.com/?jl=%E9%83%91%E5%B7%9E&kw=python&kt=3&sf=0&st=0
for page in range(page_index,page_size):
    # path = 'https://sou.zhaopin.com/?p='+str(page)+'&jl=530&kw='+kw+'&kt=3&sf=0&st=0'
    path='https://sou.zhaopin.com/?p=3&jl=530&kw=java&kt=3&sf=0&st=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    #---------下载网页-------------------
    # 设置头部信息
    request = urllib.request.Request(url=path, headers=headers)
    # 请求html
    response = urllib.request.urlopen(request)
    time.sleep(2)
    # 解析内容
    content = response.read().decode()
    print(content)
    with open('智联.html','w',encoding="utf-8") as wf:
        wf.write(content)
    #------分析页面----------------------
    #获取
    bs = BeautifulSoup(content, 'lxml',from_encoding="utf-8")
    div=bs.select('.contentpile__content__wrapper')
    print(div)
    print('-----结束page='+str(page)+'------')






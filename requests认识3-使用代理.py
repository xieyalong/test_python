

#导入包
import requests
url='https://www.baidu.com/s?wd=ip&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#代理ip
ip={
    'http':'http://112.85.165.195:9999'
}

#请求 get直接把参数放在url后面就看可以，只能获取静态页面
r=requests.get(url,headers=headers,proxies=ip)

with open(r'文件\代理.html','w',encoding='utf-8') as f:
    f.write(r.text)
print('结束')


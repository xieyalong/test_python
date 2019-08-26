

#导入包
import requests
#请求路径
url='http://www.baidu.com/s?'
# 模仿请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#请求参数，这里使用url的升级库不用在对url进行处理
data={
    'ie':'utf-8',
    'kw':'中国'
}

#请求 get直接把参数放在url后面就看可以，只能获取静态页面
r=requests.get(url,headers=headers,params=data)
print('查看对象<Response [200]>=',r)
print('查看编码=',r.encoding)
#修改编码
r.encoding='utf-8'
print('普通文字查看网页内容=',r.text)
print('二进制查看网页内容=',r.content)
print('状态码=',r.status_code)
print('查看相应头部=',r.headers)
print('查看请求的url=',r.url)
with open(r'requests\baidu.html','w',encoding='utf-8') as fw:
    fw.write(r.text)

print('结束')
#智联url路径，得异步获取
# https://sou.zhaopin.com/?p=3&jl=530&sf=0&st=0&kw=java&kt=3



#流程：登录先get获取登录数据，在进行登录
#导入包
import requests
from bs4 import  BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#访问登录页面，获取登录所需要的参数
url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes'
r=requests.get(url=url,headers=headers)
print(r.text)
print('-----登录成功-------------------------')
#把网页保存到本地
with open(r'文件\chinaunix1.html','w',encoding='utf-8') as f:
    f.write(r.text)
#解析网页
html=BeautifulSoup(r.text,'lxml')
#通过属性选择器获取登录需要的数据
formhash=html.select('input[name="formhash"]')[0]['value']
print('formhash=',formhash)
print('-----获取登录数据结束---------------')
#登录
url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes$loginhash=LAi7o'
params={
'formhash':formhash,
'referer':'http://bbs.chinaunix.net/./',
'username':'wolfmonkey',
'password':'lizhibin666',
'loginsubmit':'true',
'return_type':''
}
r=requests.post(url=url,headers=headers,data=params)
print('查看是否登录=',r.text)
print('结束')


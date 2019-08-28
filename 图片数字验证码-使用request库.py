
import  requests
import  urllib
from bs4 import  BeautifulSoup
import  time

#创建session会话
s=requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url='https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
r=s.get(url=url,headers=headers)
#解析
bs=BeautifulSoup(r.text,'lxml')
#得到图片链接保存到本地
imgCode=bs.find('img',id='imgCode')
imgPath='https://so.gushiwen.org'+imgCode['src']
print('图片路径=',imgPath)
#获取验证码图片
#直接使用urllib.request.urlretrieve(imgPath,r'文件\古文诗词验证码图片.png')
#不行，因为验证码没有在session会话范围内
#这里还是session会话对象s
img=s.get(imgPath,headers=headers)
with open(r'文件\古文诗词验证码图片.png','wb') as f_img:
    #img.content=二进制
    #img.text:普通文字
    f_img.write(img.content)

#输入验证码
code=input('输入验证码')
print('验证码=',code)
time.sleep(3)
#获取令牌
__VIEWSTATE=bs.find('input',id='__VIEWSTATE')['value']
print('令牌__VIEWSTATE=',__VIEWSTATE)
#获取令牌
__VIEWSTATEGENERATOR=bs.find('input',id='__VIEWSTATEGENERATOR')['value']
print('令牌__VIEWSTATEGENERATOR=',__VIEWSTATEGENERATOR)
#登录参数
params={
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': '17744488225',
    'pwd': 'a123456',
    'code': code,
    'denglu': '登录'
}

url_login='https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
r=s.post(url=url_login,headers=headers,params=params)
#以二进制保存
with open(r'文件\古文诗词.html','wb') as f:
    f.write(r.content)

print('网页内容=',r.text)
print('结束')















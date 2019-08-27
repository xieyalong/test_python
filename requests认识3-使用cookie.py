

#导入包
import requests
#如果碰到会话的问题，首先要创建一个会话,来保存cookie
#往下所有的请求都要用s.get或者s.post
s=requests.Session()
#地址
url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019621555628'
#请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#请求参数
params={
'rkey':    'de60e626a17db954ad57038248f290e4',
'password':    '7d281d095ab63edecdce52a7a3fe909bc38561a7b71d8a6840e5aabd845f5b00',
'origURL': 'http://www.renren.com/home',
'key_id':  '1',
'icode':'',
'f':   'http%3A%2F%2Flocalhost%3A63343%2Ftest3%2Frenren.html%3F_ijt%3Dbkjivresc5gv7ega3u1t46lr4f',
'email':   '17744488225',
'domain':  'renren.com',
'captcha_type':    'web_login'
}
#登录人人网 登录后s自动保存kookie
r=s.post(url,headers=headers,params=params)
#打印登录后的信息
print('text=',r.text)
#访问个人中心
url='http://www.renren.com/971507574/profile'
#还用要s，因为里面有kookie数据
r=s.get(url,headers=headers)
print('个人中心=',r.text)
#保存人人网的个人中心网页
with open(r'文件\人人网个人中心.html','w',encoding='utf-8') as f:
    f.write(r.text)
print('结束')


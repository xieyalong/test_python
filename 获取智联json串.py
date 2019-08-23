
#=====================================
#通过对请求路径的分析
# pageSize=90
# start=start+pageSize
#通过查看hedelr得知识get请求

#第3页
# path='https://fe-api.zhaopin.com/c/i/sou?start=180&pageSize=90&cityId=530&salary=0,0' \
#      '&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1' \
#      '&kw=java&kt=3&=0&_v=0.05588853' \
#      '&x-zp-page-request-id=ed45af16761746b19249288afaa60a7f-1565682425199-450661' \
#      '&x-zp-client-id=0714035d-524c-4564-b5f9-58d45e166f7d'

# 第4页
# https://fe-api.zhaopin.com/c/i/sou?start=270&pageSize=90&cityId=530&salary=0,0
# &workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1
# &kw=java&kt=3&=0&_v=0.62362381&x-zp-page-request-id=9bbfb20cb6f840b8847e24aae738534e-1565683130613-233554
# &x-zp-client-id=0714035d-524c-4564-b5f9-58d45e166f7d
#
# 第5页
# https://fe-api.zhaopin.com/c/i/sou?start=360&pageSize=90&cityId=530
# &salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1
# &jobWelfareTag=-1&kw=java&kt=3&=0&_v=0.62362381
# &x-zp-page-request-id=9bbfb20cb6f840b8847e24aae738534e-1565683130613-233554
# &x-zp-client-id=0714035d-524c-4564-b5f9-58d45e166f7d



#==============get请求获取字符串（智联）========================
import urllib.request
import  urllib.parse
import json
import  util.strUtil
path='https://fe-api.zhaopin.com/c/i/sou?start=180&pageSize=90&cityId=530&salary=0,0' \
     '&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1' \
     '&kw=java&kt=3&=0&_v=0.05588853' \
     '&x-zp-page-request-id=ed45af16761746b19249288afaa60a7f-1565682425199-450661' \
     '&x-zp-client-id=0714035d-524c-4564-b5f9-58d45e166f7d'
#模拟浏览器头部
headers={
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#如果有汉字需要转
# url_data=urllib.parse.urlencode(data)
#伪装头部
request=urllib.request.Request(url=path,headers=headers)
#相应
response=urllib.request.urlopen(request)
#二进制转成文字
data=response.read().decode()
# print(str)

with open('智联.json', 'w', encoding="utf-8") as f:
    json.dump(json.loads(data), f, ensure_ascii = False)
print('结束')

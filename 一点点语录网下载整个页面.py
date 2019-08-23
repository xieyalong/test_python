

import urllib.request
import  urllib.parse

# 完整路径http://mai9.net.cn/lizhi/qianming/list_50_2.html
path = 'http://mai9.net.cn/lizhi/qianming/list_50_2.html'
# 模仿请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# 设置头部信息
request = urllib.request.Request(url=path, headers=headers)
# 请求html
response = urllib.request.urlopen(request)
# 解析内容
content = response.read().decode()
print(content)
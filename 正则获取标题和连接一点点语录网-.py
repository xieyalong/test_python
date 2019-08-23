
import urllib.request
import urllib.parse
import re
import  os
import  random
import  time
import json

start_page=1
end_page=11
list=[]
#获取标题和连接
def run1():
    for i in range(start_page,end_page):
        time.sleep(2)
        #完整路径http://mai9.net.cn/lizhi/qianming/list_50_2.html
        path = 'http://mai9.net.cn/lizhi/qianming/list_50_'
        #模仿请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        #拼接连接
        path=path+str(i)+'.html'
        print('标题连接='+path)
        # 设置头部信息
        request = urllib.request.Request(url=path, headers=headers)
        # 请求html
        response = urllib.request.urlopen(request)
        # 解析内容
        content = response.read().decode()
        # print(content)
        #正则说明：
        #换行也算，这里
        patternStr = '<h3><a href="(http://mai9.net.cn/lizhi/qianming/\d+.html)">(.*?)</a></h3>'
        pattern = re.compile(patternStr)
        arr = pattern.findall(content,re.S)
        print('标题size='+str(len(arr)))
        run2(headers,arr)
        # print('数据=',list)
        print('数据size=', len(list))
        # 最后把数据写入文件
        if i == end_page-1:
            run3()
        print('------结束--i='+str(i)+'---------------')



#获取内容
def run2(headers,listData):
    for i in range(len(listData)):
        time.sleep(2)
        arr=listData[i]
        print('i='+str(i)+',连接='+str(arr[0])+',标题='+str(arr[1])+',i='+str(i))
        # path='http://mai9.net.cn/lizhi/qianming/20190841364.html'
        path=arr[0]
        request = urllib.request.Request(url=path, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode()
        #正则不知道怎么匹配，暂时只把ol下的数据拿到，然后在替换里面的标签
        pn = re.compile('<div class="neirong">(.*?)</div>', re.S)
        strArr=pn.findall(content)
        strContent=''
        #遍历获取的内容，把里面的 换行，空格，li,p,br标签替换掉
        for v in strArr:
            map = {}
            # 替换带 有<>|空格，换行
            _str = re.sub(r'<.*?>|\s', '', v)
            strContent=strContent.join(_str)
            # print(strContent)
            #设置标题
            map['title']=str(arr[1])
            #设置内容
            map['content']=strContent
            # print('map=',map)
            #把数据追加到list里面
            list.append(map)
#写入文件
def run3():
    #写入文件 默认和当前文件同级目录
    with open('一点点语录网数据.txt', 'w') as f:
        #json里面的方法，等价于f.writ()
        json.dump(list,f)
    print('写入文件成功')
#主入口
if __name__ == '__main__':
    run1()









import urllib.request
import urllib.parse
import re
import  os
import  random
import  time


#页面索引
index=1
#最大页数，只后去前10页的数据
size=10
#使用递归获取每页的html 也可以用for循环
def run():
    #调用外部变量
    global index,size
    # 完全地址 path = 'https://www.qiushibaike.com/pic/page/3/?s=5216864'
    path = 'http://www.qiushibaike.com/pic/page/'
    #模仿请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    #拼接完整页数请求路径
    path=path+str(index)+'/?s=5216864'
    #设置头部信息
    request=urllib.request.Request(url=path,headers=headers)
    #请求html
    response=urllib.request.urlopen(request)
    #解析内容
    content=response.read().decode()
    #解析html获取img的请求路径
    parseHTML(content=content)
    print('-----------结束index='+str(index)+'-----------------')
    if index<=size:
        index+=1
        run()
    else:
        print('jieshu')

#---------------------------------------------------------

#解析html获取img的请求路径
def parseHTML(content):
    # 测试：content='<div class="thumb"><a href="/article/122090391" target="_blank"><img src="//pic.qiushibaike.com/system/pictures/12209/122090391/medium/F7E6QQMV99SQGLNJ.jpg" alt="你们有没有这样的90后下属和小同事"></a></div>'
   #re.S 匹配换行在内的所有字符
    #正则“（）”就是获取（）里面的数据
    pattern=re.compile(r'<div class="thumb">.*?<img src="//(pic.qiushibaike.com/.*?)" alt=".*?">.*?</div>',re.S)
    #获取每一个"()"里面的图片路径
    #['pic.qiushibaike.com/system/pictures/12209/122090391/medium/F7E6QQMV99SQGLNJ.jpg']
    imgs=pattern.findall(content)
    print(len(imgs))
    # print(imgs)
    downloadImg(imgs)
#---------------------------------------------------------


def downloadImg(imgs):
    folder='C:\\a\\糗图'
    #判断“糗图”文件夹是否存在
    if not os.path.exists(folder):
        #创建“糗图”文件夹
        os.mkdir(folder)

    for imgUrl in imgs:
        # imgUrl = 'pic.qiushibaike.com/system/pictures/12209/122092902/medium/6UDN2GM1KGW1FPR0.jpg'
        folder = 'C:\\a\\糗图'
        #图片网路路径
        path = 'http://' + imgUrl
        #文件名称以“6UDN2GM1KGW1FPR0.jpg”
        strArr = imgUrl.split('/')
        #文件名称前面随机数
        fileName = str(random.choice(range(1000)))+strArr[len(strArr) - 1]
        #文件完整路径 'C:\\a\\糗图\\9876UDN2GM1KGW1FPR0.jpg'
        filePath=folder + '\\' + fileName
        print(fileName)
        # urlretrieve(网路地址,'文件路径')
        urllib.request.urlretrieve(path, filePath)
        #停顿1秒钟，谨防服务器识别是爬虫
        time.sleep(1)
    pass

#主入口
if __name__ == '__main__':
   run()




from  selenium import  webdriver
import  time
from bs4 import BeautifulSoup
import  json


#-----获取异步网页（动态网页）--------------
# path=r'C:\pythonWorkspace\phantomjs.exe'
path=r'C:\pythonWorkspace\chromedriver.exe'
#创建浏览器对象
# browser=webdriver.PhantomJS(path)
browser= webdriver.Chrome(executable_path=path)
url='https://sou.zhaopin.com/?p=3&jl=530&sf=0&st=0&kw=java&kt=3'
browser.get(url=url)
time.sleep(3)
#获取弹出框
div_dialog=browser.find_element_by_class_name('risk-warning__content')
#找到弹出框下的button,点击“知道了”让弹出框消失
button=div_dialog.find_element_by_tag_name('button')
#关闭弹出框事件
button.click()
time.sleep(3)
# #获取网页内容
html=browser.page_source
#把网页存到本地
with open(r'智联\智联.html','w',encoding='utf-8') as fw:
    fw.write(html)
#----bs4解析-----------
#解析本地html
# bs =BeautifulSoup(open('selenium\智联.html',encoding='UTF-8'),'lxml')
#解析网络页面
bs=BeautifulSoup(html,'lxml')
# list=bs.select('div',attrs={'class':'contentpile__content__wrapper__item clearfix'})
# print('class多个值查找,交集=',len(list))
# list=bs.select('.contentpile__content__wrapper__item,.contentpile__content__wrapper__item')
# print('class多个值查找,并集=',len(list))
list=bs.find_all('div',attrs={'class':'contentpile__content__wrapper__item clearfix'})
print('class多个值查找,并集=',len(list))

listMap=[]
for v in list:
    map = {}
    map['职位']=v.find('span',class_='contentpile__content__wrapper__item__info__box__jobname__title').text
    map['公司名称'] = v.find('a', class_='contentpile__content__wrapper__item__info__box__cname__title company_title').text
    #获取属性
    map['公司url'] =v.find('a', class_='contentpile__content__wrapper__item__info__box__cname__title company_title')['href']
    map['价格'] = v.find('p',attrs={'class':'contentpile__content__wrapper__item__info__box__job__saray'}).text
    map['地址'] = v.find_all('li', attrs={'class': 'contentpile__content__wrapper__item__info__box__job__demand__item'})[0].text
    map['年限'] = v.find_all('li', attrs={'class': 'contentpile__content__wrapper__item__info__box__job__demand__item'})[1].text.strip()
    map['学历'] = v.find_all('li', attrs={'class': 'contentpile__content__wrapper__item__info__box__job__demand__item'})[2].text
    map['公司性质'] = v.find_all('span', attrs={'class': 'contentpile__content__wrapper__item__info__box__job__comdec__item'})[0].text
    map['公司人数'] = v.find_all('span', attrs={'class': 'contentpile__content__wrapper__item__info__box__job__comdec__item'})[1].text

    fuli_list=v.find_all('div', attrs={'class': 'contentpile__content__wrapper__item__info__box__welfare__item'})
    fuli_data_list=[]
    for fuli in fuli_list:
        fuli_data_list.append(fuli.text)

    map['福利'] =fuli_data_list

    listMap.append(map)
#转json
jsonData=json.dumps(listMap,ensure_ascii=False)
print(jsonData)
#存json
with open('智联\data.json', 'w', encoding="utf-8") as f:
    json.dump(jsonData, f, ensure_ascii = False)
#关闭浏览器
browser.quit()
print('结束')









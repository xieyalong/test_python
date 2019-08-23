

from  selenium import  webdriver
import  time

# path=r'C:\pythonWorkspace\phantomjs.exe'
path=r'C:\pythonWorkspace\chromedriver.exe'
#创建浏览器对象
# browser=webdriver.PhantomJS(path)
browser= webdriver.Chrome(executable_path=path)
url='https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='
browser.get(url=url)
time.sleep(10)
browser.save_screenshot(r'phantomjs\d豆瓣1.png')
#执行js代码，模拟滚动到底部，滑动到10000
js='window.scrollTo(0,10000)'
browser.execute_script(js)
time.sleep(5)
browser.save_screenshot(r'phantomjs\d豆瓣2.png')
js='window.scrollTo(0,10000)'
browser.execute_script(js)
time.sleep(5)
browser.save_screenshot(r'phantomjs\d豆瓣3.png')
print('----结束----')
time.sleep(200)
browser.quit()









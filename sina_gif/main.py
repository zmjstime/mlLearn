# encoding:utf-8
# from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import socket

socket.setdefaulttimeout(10)


# ht = urlopen('http://gif.sina.com.cn/')
# print ht.read()


# def cbk(a, b, c):
#     '''回调函数
#     @a: 已经下载的数据块
#     @b: 数据块的大小
#     @c: 远程文件的大小
#     '''
#     per = 100.0 * a * b / c
#     if per > 100:
#         per = 100
#     print '%.2f%%' % per


url = 'http://gif.sina.com.cn/#page='
driver = webdriver.PhantomJS()

print time.localtime()
for index in xrange(1, 300):
    driver.get(url + str(index))
    driver.refresh()
    time.sleep(1)
    htobject = BeautifulSoup(driver.page_source, 'lxml')
    feedBox = htobject.find_all('div', {'class': 'gif_feed_box'})
    for x in feedBox:
        print x.a.get('href'), x.a.string
        # try:
        #     urlretrieve(x.a.get('href'), 'd:/sinagif2/' + x.a.string + '.gif')
        # except Exception as e:
        #     print 'download failed...'
    print 'page:', index, 'downloaded', url + str(index)
driver.quit()

# driver = webdriver.PhantomJS()
# ll = ['http://gif.sina.com.cn/#page=1',
#       'http://gif.sina.com.cn/#page=2']
# for x in ll:
#     print 'begin:'
#     driver.get(x)
#     driver.refresh()
#     htobject = BeautifulSoup(driver.page_source, 'lxml')
#     feedBox = htobject.find_all('div', {'class': 'gif_feed_box'})
#     for y in feedBox:
#         print y.a.get('href'), y.a.string, x
#     print 'end'
#     driver.delete_all_cookies()
# driver.quit()

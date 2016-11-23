# from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
import time


# ht = urlopen('http://gif.sina.com.cn/')
# print ht.read()


url = 'http://gif.sina.com.cn/#page='

for index in xrange(100, 300):
    driver = webdriver.PhantomJS()
    driver.get(url + str(index))
    time.sleep(2)
    htobject = BeautifulSoup(driver.page_source, 'lxml')
    feedBox = htobject.find_all('div', {'class': 'gif_feed_box'})
    for x in feedBox:
        print x.a.get('href'), x.a.string
        try:
        	urlretrieve(x.a.get('href'), x.a.string + '.gif')
        except Exception as e:
	        print 'download failed...'
    print 'page:', index, 'downloaded', url + str(index)
    driver.close()


# driver = webdriver.PhantomJS()
# driver.get(url)
# time.sleep(2)
# htobject = BeautifulSoup(driver.page_source, 'lxml')
# feedBox = htobject.find_all('div', {'class': 'gif_feed_box'})
# for x in feedBox:
#     print x.a.get('href'), x.a.string
#     urlretrieve(x.a.get('href'), x.a.string + '.gif')
# print 'page:', 'downloaded', url
# driver.close()

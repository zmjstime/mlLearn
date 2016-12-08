# encoding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver


def getTagUrlDict(url):
    urlDict = {}
    urlObject = webdriver.PhantomJS()
    urlObject.get(url)
    soupObject = BeautifulSoup(urlObject.page_source, 'lxml')
    tagCols = soupObject.find_all('table', {'class': 'tagCol'})
    for tagType in tagCols:
        typeName = tagType.find_previous_sibling('a').get('name')
        tags = tagType.find_all('a')
        tagUrls = []
        for tagA in tags:
            tagUrls.append('https://book.douban.com' + tagA.get('href'))
            # print 'https://book.douban.com' + tagA.get('href')
        urlDict[typeName] = tagUrls
    urlObject.quit()
    return urlDict

# encoding:utf-8
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
# from urlGet import getTagUrlDict

reload(sys)
sys.setdefaultencoding('utf-8')


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


def getPageInfo(url):
    pageInfo = {}
    htmlText = urllib2.urlopen(url).read()
    soupObject = BeautifulSoup(htmlText, 'lxml')
    subjectLists = soupObject.find_all('li', {'class': 'subject-item'})
    for subjectList in subjectLists:
        # print subjectList.find('img').get('src')
        try:
            bookTitle = ''.join(list(subjectList.find(
                'div', {'class': 'info'}).a.strings))
            pageInfo['bookTitle'] = ''.join(bookTitle.split())
            pageInfo['publish'] = subjectList.find(
                'div', {'class': 'pub'}).string
            pageInfo['ratingNums'] = subjectList.find(
                'span', {'class': 'rating_nums'}).string
            pageInfo['personNums'] = subjectList.find(
                'span', {'class': 'pl'}).string
            pageInfo['brief'] = subjectList.p.string
        except Exception:
            print 'parse error!'
    span = soupObject.find('span', {'class': 'next'})
    if span is None:
        print 'this is the last page!'
        return pageInfo, None
    return pageInfo, 'https://book.douban.com' + span.a.get('href').encode('utf-8')


def getTagInfo(tagDict):
    for tag in tagDict:
        for url in tagDict[tag]:
            pageInfo, url = getPageInfo(url.encode('utf-8'))
            while url:
                pageInfo, url = getPageInfo(url.encode('utf-8'))
                print url


if __name__ == '__main__':
    # tagDict = getTagUrlDict('https://book.douban.com/tag/?icn=index-nav')
    # tagDict = getTagUrlDict('https://book.douban.com')
    getPageInfo('https://book.douban.com/tag/小说')
    # getTagInfo(tagDict)

# urlObject = webdriver.PhantomJS()
# urlObject.get('https://book.douban.com/tag/小说')
# time.sleep(3)
# soupObject = BeautifulSoup(urlObject.page_source, 'lxml')
# print urlObject.page_source


# info, url = getPageInfo('https://book.douban.com/tag/小说')
# print info['bookTitle']
# print info['publish']
# print info['ratingNums']
# print info['personNums']
# print info['brief']
# print info.get('bookTitle')
# for x in info:
#     # print 's', info[x]
#     print '', info[x].strip()
# print url

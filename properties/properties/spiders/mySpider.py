from bs4 import BeautifulSoup
from scrapy import Spider
from scrapy.loader import ItemLoader
import sys
sys.path.insert(0, '../../')
from properties.items import PropertiesItem
from scrapy.loader.processors import MapCompose, Join

reload(sys)
sys.setdefaultencoding("utf-8")


class MySpider(Spider):
    name = 'mySpider'
    allowed_domains = ["gif.sina.com.cn"]
    start_urls = ['http://gif.sina.com.cn/']

    def parse(self, response):
        loaders = ItemLoader(item=PropertiesItem(), response=response)

        htobject = BeautifulSoup(response.body, 'lxml')
        feedBox = htobject.find_all('div', {'class': 'gif_feed_box'})
        for x in feedBox:
            loaders.add_value(
                'imgInfo', {'title': x.a.string, 'imgUrl': x.a.get('href')})

        # loaders.add_xpath('imgUrl', '//*[@id="gif_feed_wrap"]/div[2]/h2/a/@href',
        #                   MapCompose(unicode.strip, unicode.title))
        # loaders.add_xpath('title', '//*[@id="gif_feed_wrap"]/div[2]/h2/a/text()',
        #                   MapCompose(unicode.strip, unicode.title))
        # loaders.add_value('imgUrl', response.url)

        # print response.body
        return loaders.load_item()

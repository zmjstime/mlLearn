from bs4 import BeautifulSoup
from scrapy import Spider
from scrapy.loader import ItemLoader
import sys
sys.path.insert(0, '../../')
from properties.items import PropertiesItem
from scrapy.loader.processors import MapCompose, Join
from scrapy.http import Request

reload(sys)
sys.setdefaultencoding("utf-8")


class MySpider(Spider):
    name = 'mySpider'
    allowed_domains = ["gif.sina.com.cn"]
    start_urls = ['http://gif.sina.com.cn/#page=2']

    def parse(self, response):
        for x in xrange(1, 10):
            yield Request('http://gif.sina.com.cn/#page=%s' % x, callback=self.parse_item)

    def parse_item(self, response):
        loaders = ItemLoader(item=PropertiesItem(), response=response)

        htobject = BeautifulSoup(response.body, 'lxml')
        feedBox = htobject.find_all('div', {'class': 'gif_feed_box'})
        for x in feedBox:
            loaders.add_value(
                'imgInfo', {'title': x.a.string, 'imgUrl': x.a.get('href')})

        yield loaders.load_item()

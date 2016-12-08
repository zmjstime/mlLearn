from scrapy import Spider
from scrapy.loader import ItemLoader
import sys
sys.path.insert(0, '../../')
from properties.items import PropertiesItem
from scrapy.loader.processors import MapCompose, Join


class MySpider(Spider):
    name = 'mySpider'
    allowed_domains = ["gif.sina.com.cn"]
    start_urls = ['http://gif.sina.com.cn/']

    def parse(self, response):
        loaders = ItemLoader(item=PropertiesItem(), response=response)

        loaders.add_xpath('imgUrl', '//*[@id="gif_feed_wrap"]/div[2]/h2/a/@href',
                          MapCompose(unicode.strip, unicode.title))
        loaders.add_xpath('title', '//*[@id="gif_feed_wrap"]/div[2]/h2/a/text()',
                          MapCompose(unicode.strip, unicode.title))
        # loaders.add_value('imgUrl', response.url)

        # print response.body
        return loaders.load_item()

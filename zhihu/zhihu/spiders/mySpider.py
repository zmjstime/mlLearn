from scrapy.spiders import Spider
# from scrapy.spiders import Rule
# from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
import sys
sys.path.insert(0, '../../')
from zhihu.items import ZhihuItem


class MySpider(Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = (
        'https://www.zhihu.com/',
    )

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"next")]')),
    #     Rule(LinkExtractor(restrict_xpaths='//*[@id="feed-0"]/div[1]/div[2]/div[2]/h2/a/@href'),
    #          callback='parse_item')
    # )

    def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = ItemLoader(item=ZhihuItem(), response=response)
        item.add_xpath('name', '//*[@id="feed-5"]/div[1]/div[2]/div[2]/h2/a')

        return item.load_item()

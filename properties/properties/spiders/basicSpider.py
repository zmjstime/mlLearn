# -*- coding: utf-8 -*-
import scrapy
# from scrapy.loader import ItemLoader
import sys
sys.path.append('../../')
from properties.items import PropertiesItem
# from scrapy.http import Request


class BascispiderSpider(scrapy.Spider):
    name = "basicSpider"
    allowed_domains = ["web"]
    start_urls = ['http://www.baidu.com.cn/']
    # start_urls = ['http://gif.sina.com.cn/']

    def parse(self, response):
        item = PropertiesItem()
        item['title'] = req.xpath(
            '//*[@id="u1"]/a[2]/text()').extract()
        item['imgUrl'] = req.xpath(
            '//*[@id="u1"]/a[2]/@href').extract()

        # print '_____', item['title'], '_______', item['imgUrl']

        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class XianaqiItem(Item):
    city = Field()
    date = Field()
    aqi = Field()
    ranges = Field()
    level = Field()
    pm25 = Field()
    pm10 = Field()
    so2 = Field()
    co = Field()
    no2 = Field()
    o3 = Field()
    rank = Field()

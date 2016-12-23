# encoding:utf-8
from bs4 import BeautifulSoup
from scrapy import Spider
from scrapy.http import Request
import sys
sys.path.insert(0, '../../')
from xianAQI.items import XianaqiItem


class AQICrawl(Spider):
    name = 'xianaqi'
    start_urls = ['http://www.aqistudy.cn/historydata/monthdata.php?city=西安',
                  ]

    def parse(self, response):
        htmlObject = BeautifulSoup(response.body, 'lxml')
        table = htmlObject.find('table')
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) != 11:
                continue
            for td in tds:
                urlTd = td.find_all('a')
                if len(urlTd):
                    newUrl = 'http://www.aqistudy.cn/historydata/' + \
                        urlTd[0].get('href')
                    yield Request(newUrl, callback=self.parse)
            print len(tr)
            item = XianaqiItem()
            item['city'] = 'xian'
            item['date'] = tds[0].string
            item['aqi'] = tds[1].string
            item['ranges'] = tds[2].string
            item['level'] = tds[3].string
            item['pm25'] = tds[4].string
            item['pm10'] = tds[5].string
            item['so2'] = tds[6].string
            item['co'] = tds[7].string
            item['no2'] = tds[8].string
            item['o3'] = tds[9].string
            item['rank'] = tds[10].string
            yield item

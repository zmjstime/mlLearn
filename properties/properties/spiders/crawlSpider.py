import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# help(LinkExtractor)
# help(Rule)


class CrawlByRules(CrawlSpider):
    name = 'crawlSina'
    allowed_domains = ["gif.sina.com.cn"]
    start_url = ('http://gif.sina.com.cn')
    # rules = (
    #     Rule(LinkExtractor(allow=('.*gif.sina.com.cn.*'))),
    #     Rule(LinkExtractor(restrict_xpaths='//*[@id="gif_feed_wrap"]/div[1]/div[1]/a[1]/img'),
    #                        callback='parse_item', follow=True)
    #     )

    def parse(self, response):
        print '**********************************************'
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

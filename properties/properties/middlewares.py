from selenium import webdriver
from scrapy.http import HtmlResponse


class MyCustomDownloaderMiddleware(object):

    def process_request(self, request, spider):
        driver = webdriver.PhantomJS()
        driver.get(request.url)
        body = driver.page_source

        return HtmlResponse(driver.current_url, body=body,
                            encoding='utf-8', request=request)

import scrapy
from wexin01.items import Wexin01Item
class wxscrapy01(scrapy.Spider):
    name = "wxscrapy01"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://weixin.sogou.com/"]

    def parse(self, response):
        sels = response.xpath('//div[@class="wx-news-info2"]')
        for sel in  sels:
            item = Wexin01Item()
            titles = sel.xpath('.//h4//a/text()').extract()
            for title in titles:
                item['title'] = title
            hrefs = sel.xpath('.//h4//a/@href').extract()
            for href in hrefs:
                item['href'] = href
            yield item

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from myimage_crwaler.items import MyimageCrwalerItem

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


class ImageSpider(scrapy.Spider):
    name = "image"
    allowed_domains = ["netbian.com"]
    start_urls = (
        'http://www.netbian.com/jianzhu/',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=hdr)

    def parse(self, response):
        # for link in response.xpath('//a'):
        #     item = MyimageCrwalerItem()
            # item['image_urls'] = link.xpath('img/@src').re(r'.*jpg$')
        item = MyimageCrwalerItem()
        item['image_urls'] = response.xpath('//*/@data-src').extract()
        yield item
#-*- coding: UTF-8 -*-
from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector
from mianwww.items import DmozItem

class MianwwwSpider(Spider):
    name = "mianwww"
    allowed_domians = ['mianwww.com']
    start_urls = []
    def __init__(self):
        url = "http://www.mianwww.com/html/category/it-interview/java/page/"
        for index in range(52):
            self.start_urls.append(url + str(index + 1))

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="post"]/div[@class="entry"]/h2')
        items = []
        for site in sites:
            item = DmozItem()
            item['link'] = site.xpath('a/@href').extract()[0];
            item['title'] = site.xpath('a/text()').extract()[0];
            items.append(item)
        return items

    def print_urls(self):
        for url in self.start_urls:
            print url

if __name__ == '__main__':
    mianwww = MianwwwSpider()
    mianwww.print_urls()





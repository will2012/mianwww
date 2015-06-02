#-*- coding: UTF-8 -*-
from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector
from mianwww.items import DmozItem
from mianwww.items import Post
import json

class MianwwwSpider(Spider):
    name = "mianwww_post"
    allowed_domians = ['mianwww.com']
    start_urls = []
    def __init__(self):
        filepath = "softtest_items.json"
        self.spiderContents(filepath)

    def spiderContents(self, filepath):
        file_object = open(filepath)
        try:
             jsonstr = file_object.read()
             array = json.loads(jsonstr)
             for item in array:
                 self.start_urls.append(item['link'])
        finally:
             file_object.close()


    def parse(self, response):
        sel = Selector(response)
        post = sel.xpath('//div[@class="post"]')
        title = post[0].xpath('h3/a/text()').extract()[0]
        contents = post[0].xpath('div[@class="single-post-content"]/p/text()').extract()
        item = Post()
        item['title'] = title
        item['contents'] = contents
        return item

def print_urls(self):
        for url in self.start_urls:
            print url

if __name__ == '__main__':
    mianwww = MianwwwSpider()
    mianwww.print_urls()





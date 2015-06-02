#-*- coding: UTF-8 -*-
from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector
from mianwww.items import DmozItem
from mianwww.items import Post
import json

class MianwwwSpider(Spider):
    name = "mianwww"
    allowed_domians = ['mianwww.com']
    start_urls = []
    def __init__(self):
        #url = "http://www.mianwww.com/html/category/it-interview/java/page/"
        #url = "http://www.mianwww.com/html/category/it-interview/linux-it-interview/page/"
        #url = "http://www.mianwww.com/html/category/it-interview/c-it-interview/page/";
        #url = "http://www.mianwww.com/html/category/it-interview/mobile/page/";
        #url = "http://www.mianwww.com/html/category/it-interview/android/page/"
        #url = "http://www.mianwww.com/html/category/it-interview/cpp/page/"
        url = "http://www.mianwww.com/html/category/it-interview/softwaretest/page/"
        self.spiderUrls(url)

    def spiderUrls(self, url):
        for index in range(23):
            self.start_urls.append(url + str(index + 1))

    def spiderContents(self, filepath):
       # filepath = "c_items.json"
       # filepath = "android_items.json"
       # filepath = "ios_items.json"
       # filepath = "java_items.json"
       # filepath = "linux_items.json"
        file_object = open(filepath)
        try:
             jsonstr = file_object.read()
             array = json.loads(jsonstr)
             for item in array:
                 self.start_urls.append(item['link'])
        finally:
             file_object.close()


    #def parse(self, response):
    #    sel = Selector(response)
    #    post = sel.xpath('//div[@class="post"]')
    #    title = post[0].xpath('h3/a/text()').extract()[0]
    #    contents = post[0].xpath('div[@class="single-post-content"]/p/text()').extract()
    #    item = Post()
    #    item['title'] = title
    #    item['contents'] = contents
    #    return item

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="post"]/div[@class="entry"]/h2')
        items = []
        for site in sites:
            item = DmozItem()
            item['link'] = site.xpath('a/@href').extract()[0];
            #item['title'] = site.xpath('a/text()').extract()[0];
            items.append(item)
        return items

    def print_urls(self):
        for url in self.start_urls:
            print url

if __name__ == '__main__':
    mianwww = MianwwwSpider()
    mianwww.print_urls()





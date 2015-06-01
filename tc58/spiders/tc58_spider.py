#!/usr/bin/env python
# encoding: utf-8
import scrapy
from scrapy.http import Request

from tc58.items import Tc58Item

class DmozSpider(scrapy.Spider):
    name = "tc58"
    allowed_domains = ["58.com"]
    start_urls = []
    for i in range(1,7):
        start_urls.append("http://nj.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://nj.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://su.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://su.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://wx.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://wx.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://cz.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://cz.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://xz.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://xz.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://nt.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://nt.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://yz.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://yz.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://yancheng.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://yancheng.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://ha.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://ha.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://lyg.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://lyg.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://taizhou.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://taizhou.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://suqian.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://suqian.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://zj.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://zj.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://shuyang.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://shuyang.58.com/ershouche/1/pn" + str(i) + "/?")
        start_urls.append("http://dafeng.58.com/ershouche/0/pn" + str(i) + "/?")
        start_urls.append("http://dafeng.58.com/ershouche/1/pn" + str(i) + "/?")

    def parse(self, response):
        if 'ershouche/0/pn' in response.url:
            is_seller = '个人'
        elif 'ershouche/1/pn' in response.url:
            is_seller = '商家'
        for sel in response.xpath("//div[@id='infolist']/table[@class='tbimg']"):
            for tr in sel.xpath('tr'):
                urls = tr.xpath('td[2]/a[@class="t"]/@href').extract()
                for url in urls:
                    #item = Tc58Item()
                    #item['title'] = tr.xpath('td[2]/a[@class="t"]/text()').extract()
                    #item['link'] = tr.xpath('td[2]/a[@class="t"]/@href').extract()
                    #item['price'] = tr.xpath('td[3]/b/text()').extract()
                    yield Request(url, meta={'is_seller':is_seller},callback = self.parse2)

    def parse2(self, response):
        items = []
        item = Tc58Item()
        for sel in response.xpath("//div[@id='content_sumary_right']"):
            tele = ''
            item['title'] = sel.xpath("h1[@class='h1']/text()").extract()
            item['config'] = sel.xpath("h2[@class='h2']/text()").extract()
            item['price'] = sel.xpath("div[@id='content_price']/div[@class='content_price_left']/p[1]/span[@class='font_jiage']/text()").extract()
            contacts = sel.xpath("p[@class='lineheight_2']/span[@class='left_title']/text()").extract()
            for contact in contacts:
                if contact == u'联系':
                    item['name'] = sel.xpath("p[@class='lineheight_2']/span[2]/a/text()").extract()
                elif contact == u'电话':
                    for tel in sel.xpath("p[@class='lineheight_2']/span[2]/text()").extract():
                        tele += tel
                    item['telephone'] = [tele.replace(' ','')]
            item['address'] = sel.xpath("p[@class='lineheight_2 relative']/span[@id='address_detail']/text()").extract()
            item['link'] = response.url
            item['release_time'] = sel.xpath("div[@class='mtit_con c_999 f12 clearfix']/ul[1]/li/text()").extract()
            item['is_seller'] = [response.meta['is_seller']]
            items.append(item)
            print item['telephone']
            #yield item
        return items




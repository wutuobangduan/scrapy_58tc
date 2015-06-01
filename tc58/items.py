# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tc58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    config = scrapy.Field()
    name = scrapy.Field()
    telephone = scrapy.Field()
    address = scrapy.Field()
    release_time = scrapy.Field()
    is_seller = scrapy.Field()

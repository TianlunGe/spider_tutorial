# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class douban_movie_item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie = scrapy.Field()
    link = scrapy.Field()
    rate = scrapy.Field()


class balance_item(scrapy.Item):
    stock_name = scrapy.Field()
    date = scrapy.Field()
    资产总额 = scrapy.Field()
    流动资产总额 = scrapy.Field()
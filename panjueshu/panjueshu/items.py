# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PanjueshuItem(scrapy.Item):
    name=scrapy.Field()
    type=scrapy.Field()
    num=scrapy.Field()
    court=scrapy.Field()
    date=scrapy.Field()
    url=scrapy.Field()
    docid=scrapy.Field()
    produce=scrapy.Field()
    yiju=scrapy.Field()
    content=scrapy.Field()  

class LiaoItem(scrapy.Item):
    context=scrapy.Field()

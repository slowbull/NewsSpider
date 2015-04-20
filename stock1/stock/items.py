# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item,Field
#import scrapy

class StockItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = Field(serializer = str)
    name = Field(serializer = str)
    pe = Field(serializer = str)
    pb = Field(serializer = str)
    value = Field(serializer = str)

class StockIndustry(Item):
    code = Field(serializer = str)
    industry = Field(serializer = str)

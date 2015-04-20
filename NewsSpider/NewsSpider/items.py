#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field

class NewsspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_name = Field(serializer=str)
    article_body = Field(serializer=str)
    article_url = Field(serializer=str)
    article_time = Field(serializer=str)
    ID = Field(serializer=str)

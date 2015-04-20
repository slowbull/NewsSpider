#!/usr/bin/env python
#-*- coding:utf-8 -*-

#!!! read me!!!!
# use url.py to define the crawled websites. 
# overide parse, and let spider run to find articles and find pages.
# use the unique id in mysql to avoid replicate similar pages. 

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from NewsSpider.items import NewsspiderItem
from time import strftime,gmtime
import time
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
import re
import url

class NewsSpider(Spider):
    name = 'NewsSpider'
    download_delay = 0.3
    allowed_domains = ['eastmoney.com']
    start_urls = url.url1+url.url2

# parse 1. find page url to return to parse method.
#	2. find article url to return to parse_article method. 
    def parse(self,response):	
	sel = Selector(response)
	item = NewsspiderItem()
	article_url = str(response.url)
	newsTime = strftime('%m%d',gmtime())   # define article time
	urls = sel.xpath('//@href').extract()
        # change to _0.html to make this whole article show in one page.	
	for url in urls: 
	    if url.count(newsTime) > 0:
	        url = url.replace('.html','_0.html')
	        yield Request(url,callback=self.parse_article)
	# find pages urls
	for url in urls:        
	    if url.count('/') == 0:
	        pattern = re.compile(r'http://.*/')
	        match = pattern.match(article_url)
	        url = match.group() + url
	# just search 10 pages.
	        for i in url:
	            if '0' < i <='10':
	       	        yield Request(url,callback=self.parse) 
   
 # parse article pages. and return item to pipeline. 
    def parse_article(self,response):
	sel = Selector(response)
	item = NewsspiderItem()
	article_url = str(response.url)
	newsTime = strftime('%y%m%d',gmtime())   # define article time
	yearday = time.gmtime().tm_yday
	# check if this page is an article, if yes parse it.
	if True:
	    article_name = \
		sel.xpath('//div[@class="newText new"]/h1/text()').extract()
	    article_time = \
		sel.xpath('//div[@class="Info"]/span/text()').extract()
	    article_body = sel.xpath('//div[@id="ContentBody"]/p/text()').extract()
	    item['article_name'] = article_name[0]
	    item['article_time'] = article_time[0]
	    item['ID'] = yearday
	    item['article_url'] = article_url
	    item['article_body'] = [''.join(n for n in article_body)][0]
	    yield item
         

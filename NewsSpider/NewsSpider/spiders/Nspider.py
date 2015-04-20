#!/usr/bin/env python
#-*- coding: utf-8 -*-

#some pages could'nt be crawled,but some can.

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from NewsSpider.items import NewsspiderItem
from time import strftime,gmtime
import time
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
import re

class NewsSpider(CrawlSpider):
    name = 'NewsSpider1'
    download_delay = 0.3
    allowed_domains = ['finance.sina.com.cn','finance.qq.com','eastmoney.com','money.163.com','finance.ifeng.com']
    start_urls=['http://eastmoney.com']
    rules = (Rule(LinkExtractor(allow=('stock.eastmoney','finance.eastmoney',)),callback='parse_eastmoney',follow=True),)

    def parse_eastmoney(self,response):
	sel = Selector(response)
	item = NewsspiderItem()
	article_url = str(response.url)
	newsTime = strftime('%m%d',gmtime())   # define article time
	# check if this page is an article, if yes parse it.

	if article_url.count(newsTime) > 0 and len(sel.xpath('//div[@class="newText new"]/h1/text()').extract()) > 0:
	    article_name = \
		sel.xpath('//div[@class="newText new"]/h1/text()').extract()
	    article_time = \
		sel.xpath('//div[@class="Info"]/span/text()').extract()
	    article_body = sel.xpath('//div[@id="ContentBody"]/p/text()').extract()
	    item['article_name'] = article_name[0]
	    item['article_time'] = article_time[0]
	    item['article_url'] = article_url
	    item['article_body'] = [''.join(n for n in article_body)][0]
	    yield item

"""    def parse_article(self,response):
	sel = Selector(response)
	item = NewsspiderItem()
	article_url = str(response.url)
	print '=======',article_url
	newsTime = strftime('%m%d',gmtime())   # define article time
	# check if this page is an article, if yes parse it.
	if article_url.count(newsTime) > 0 and article_url.count('_0') > 0 and len(sel.xpath('//div[@class="newText new"]/h1/text()').extract()) > 0:
	    article_name = \
		sel.xpath('//div[@class="newText new"]/h1/text()').extract()
	    article_time = \
		sel.xpath('//div[@class="Info"]/span/text()').extract()
	    article_body = sel.xpath('//div[@id="ContentBody"]/p/text()').extract()
	    item['article_name'] = article_name[0]
	    item['article_time'] = article_time[0]
	    item['article_url'] = article_url
	    item['article_body'] = [''.join(n for n in article_body)][0]
	    yield item
        # make this whole article show in one page.	
	elif article_url.count(newsTime) > 0 and article_url.count('_0') == 0 and len(sel.xpath('//div[@class="newText new"]/h1/text()').extract()) > 0:
	    url = article_url.replace('.html','_0.html')
	    print '------------',url
	    yield Request(url,callback=self.parse_eastmoney)
     
	#parse the urls in this page 
	elif article_url.count('stock.eastmoney')>0 or article_url.count('finance.eastmoney')>0:
	    urls = sel.xpath('//@href').extract()
	    for url in urls: 
	        if url.count('/') == 0:
		    pattern = re.compile(r'http://.*/')
		    match = pattern.match(article_url)
		    url = match.group() + url
	       	    yield Request(url,callback=self.parse_eastmoney) 
"""
"""
    def parse_ifeng(self,response):
	sel = Selector(response)
	item = NewsspiderItem()
	article_url = str(response.url)
	newsTime = strftime('%m%d',gmtime())
	print '-----------------------',response.url
	if article_url.count(newsTime) > 0 and len(sel.xpath('//h1[@id="artical_topic"]/text()').extract()) > 0:
	    print '++++++++++++++++++++++',response.url
	    article_name = \
		sel.xpath('//h1[@id="artical_topic"]/text()').extract()
	    article_time = \
		sel.xpath('//p[@class="p_time"]/span[@class="ss01"]/text()').extract()
	    article_body = sel.xpath('//div[@id="main_content"]/p/text()').extract()
	    item['article_name'] = article_name[0]
	    item['article_time'] = article_time[0]
	    item['article_url'] = article_url
	    item['article_body'] = [''.join(n for n in article_body)][0]
	    yield item	
	else:
	    urls = sel.xpath('//@href').extract()
	    newsTime = strftime('%m%d',gmtime())
	    for url in urls:
	        if url.count('finance.ifeng') > 0:
	   	    yield Request(url,callback=self.parse)  
   
    def parse_sina(self,response):
	sel = Selector(response)
	item = NewsspiderItem()
	if len(sel.xpath('//div/h1[@id="artibodyTitle"]/text()').extract()) > 0:
	    article_url = str(response.url)
	    article_name = \
		sel.xpath('//div/h1[@id="artibodyTitle"]/text()').extract()
	    article_time = \
		sel.xpath('//div/span[@id="pub_date"]/text()').extract()
	    article_body = sel.xpath('//div[@id="artibody"]/p/text()').extract()
	    #item['article_name'] = [n.encode('utf-8') for n in article_name]
            #item['article_time'] = [n.encode('utf-8') for n in article_time]
	    #item['article_url'] = article_url.encode('utf-8')
	    #item['article_body'] = [''.join(n.encode('utf-8') for n in article_body)]
	    item['article_name'] = article_name[0]
	    item['article_time'] = article_time[0]
	    item['article_url'] = article_url
	    item['article_body'] = [''.join(n for n in article_body)][0]
	    yield item	
        
	urls = sel.xpath('//@href').extract()
	newsTime = strftime('%m%d',gmtime())
	for url in urls:
	    if (url.count('finance') > 0 ) and url.count(newsTime) > 0 :
		yield Request(url,callback=self.parse)  
   
    def parse_qq(self,response):
	sel = Selector(response)
	item = NewsspiderItem()
	if len(sel.xpath('//div[@class="hd"]/h1/text()').extract()) > 0:
	    article_url = str(response.url)
	    article_name = \
		sel.xpath('//div[@class="hd"]/h1/text()').extract()
	    article_time = \
		sel.xpath('//span[@class="pubTime article-time"]/text()').extract()
	    article_body = sel.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract()
	    item['article_name'] = article_name[0]
	    item['article_time'] = article_time[0]
	    item['article_url'] = article_url
	    item['article_body'] = [''.join(n for n in article_body)][0]
	    yield item	
        
	urls = sel.xpath('//@href').extract()
	newsTime = strftime('%m%d',gmtime())
	for url in urls:
	    if (url.count('finance') > 0) and url.count(newsTime) > 0 :
		yield Request(url,callback=self.parse)  

"""

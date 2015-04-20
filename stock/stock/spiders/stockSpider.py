#-*- coding: utf-8 -*-

from scrapy.http import Request
from scrapy.selector import Selector
from stock.items import StockItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
import re

class stockSpider(CrawlSpider):
    name = 'stockSpider'
    download_delay = 0.5
    allowed_domains = ['eastmoney.com']
    start_urls = ["http://quote.eastmoney.com/stocklist.html",]
    rules = (
	Rule(LinkExtractor(allow = ('stocklist',)),callback = 'parse_item'),
	Rule(LinkExtractor(allow = ('sh6\d{5}','sz3\d{5}','sz0\d{5}')),callback = 'parse_stock'),)

    def parse_item(self,response):
	selector = Selector(response)
	for link in selector.xpath("//div[@id='quotesearch']/ul/li/a/@href").extract():
	    if(link.count('sh6') > 0 or link.count('sz3') > 0 or link.count('sz0')>0):	
	        yield Request(link,callback=self.parse_stock)

    def parse_stock(self,response):
	selector = Selector(response)
 	stocks = StockItem()
 	stocks_code = selector.xpath("//div/b[@id='code']/text()").extract()
	stocks_name = selector.xpath("//div/h2[@id='name']/text()").extract()
 	stocks_pe = selector.xpath("//td/span[@id='gt6_2']/text()").extract()
	stocks_pb = selector.xpath("//td/span[@id='gt13_2']/text()").extract()
	stocks_value = selector.xpath("//td/span[@id='gt14_2']/text()").extract()
	stocks['code'] = stocks_code[0]
	stocks['name'] = stocks_name[0]
	stocks['pe'] = stocks_pe[0]
	stocks['pb'] = stocks_pb[0]
	stocks['value'] = stocks_value[0]
	yield stocks    


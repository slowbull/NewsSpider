# -*- coding: utf-8 -*-

# Scrapy settings for stock project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'stockSpider'
COOKIES_ENABLED = False
SPIDER_MODULES = ['stock.spiders']
NEWSPIDER_MODULE = 'stock.spiders'
ITEM_PIPELINES = {'stock.pipelines.StockPipeline':300}
DEPTH_LIMIT = 5
CONCURRENT_REQUESTS = 100
#LOG_LEVEL = 'INFO'
DOWNLOAD_TIMEOUT = 20
#SPIDER_MIDDLEWARES = {'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware':None}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stock (+http://www.yourdomain.com)'

# -*- coding: utf-8 -*-
# Scrapy settings for NewsSpider project #
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here: #
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'NewsSpider'
COOKIES_ENABLED = False
SPIDER_MODULES = ['NewsSpider.spiders']
NEWSPIDER_MODULE = 'NewsSpider.spiders'
ITEM_PIPELINES = {'NewsSpider.pipelines.NewsspiderPipeline':300}
DEPTH_LIMIT = 3
CONCURRENT_REQUESTS = 100
LOG_LEVEL = 'CRITICAL'
DOWNLOAD_TIMEOUT = 5

"""
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
"""
#USER_AGENT = 'NewsSpider (+http://www.yourdomain.com)'

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import json
#import codecs
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class NewsspiderPipeline(object):
    def __init__(self):
	#self.newsfile = codecs.open('News.json',mode = 'wb',encoding='utf-8') 
   	self.dbpool = adbapi.ConnectionPool('MySQLdb',
	    db = 'newsInfo',
	    user = 'root',
	    passwd = 'hzy387hzy',
	    cursorclass = MySQLdb.cursors.DictCursor,
	    charset = 'utf8',
	    use_unicode = False)
	
    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + '\n' 
	#self.newsfile.write(line.decode('unicode_escape'))
	query = self.dbpool.runInteraction(self._conditional_insert,item)
	return item

    def _conditional_insert(self,tx,item):
	sql = 'insert into article values(%s,%s,%s,%s,%s)'
	tx.execute(sql,(item['article_name'],item['article_time'],item['article_body'],item['article_url'],item['ID'])) 


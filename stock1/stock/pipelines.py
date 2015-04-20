# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# update type of industry

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from stock.items import StockItem,StockIndustry

class StockPipeline(object):
    def __init__(self):
	self.dbpool = adbapi.ConnectionPool('MySQLdb',
	    db = 'stock',
	    user = 'root',
	    passwd = 'hzy387hzy',
	    cursorclass = MySQLdb.cursors.DictCursor,
	    charset = 'utf8',
	    use_unicode = False)

    def process_item(self, item, spider):
        if isinstance(item,StockItem):
	    query = self.dbpool.runInteraction(self._conditional_insert,item)
	elif isinstance(item,StockIndustry): 
	    query = self.dbpool.runInteraction(self._conditional_insert1,item)
	return item
	
    def _conditional_insert(self,tx,item):
	#sql = 'insert into stocktable values (%s,%s,%s,%s,%s)'
	sql = 'insert into stocktable (code,name,pe,pb,value) values(%s,%s,%s,%s,%s)'
	tx.execute(sql,(item['code'],item['name'],item['pe'],item['pb'],item['value']))

    # insert contents in F10
    def _conditional_insert1(self,tx,item):
	sql = "update stocktable set industry=%s where code=%s"
	print '++++++++++++++++++++++++++++++++',item['code'],item['industry']
	tx.execute(sql,(item['industry'],item['code']))



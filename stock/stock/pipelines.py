# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

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
        query = self.dbpool.runInteraction(self._conditional_insert,item)
	return item

    def _conditional_insert(self,tx,item):
	#sql = 'insert into stocktable values (%s,%s,%s,%s,%s)'
	sql = 'update stocktable set pe=%s,pb=%s,value=%s where code=%s'
	tx.execute(sql,(item['pe'],item['pb'],item['value'],item['code']))


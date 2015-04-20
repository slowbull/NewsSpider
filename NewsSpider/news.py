#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1. store three days' news in mysql.
# 2. crawl new news and insert to mysql.


import MySQLdb
import MySQLdb.cursors
import time
from scrapy.cmdline import execute as ex

db = MySQLdb.connect(db='newsInfo',user='root',passwd='hzy387hzy',charset='utf8')
c = db.cursor()

yday = time.gmtime().tm_yday
# delete news in week 2,3,4,5, maintain 6,7
if yday > 3:
    cmd = 'delete from article where ID<='+str(yday-3)
else:
    cmd = 'delete from article where ID<=' + str(yday+365-3)

try: 
    c.execute(cmd)
    db.commit()
except:
    db.rollback()

db.close()

ex(['scrapy','crawl','NewsSpider'])



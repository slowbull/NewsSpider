#!usr/bin/env python
#-*- coding = utf-8 -*-

"""
usage: use jieba.package to do text segmentation
"""

import MySQLdb
import jieba
import jieba.analyse
import codecs

# import new dictionary for parse
jieba.load_userdict('Dict.txt')

db = MySQLdb.connect(host='localhost',
	user = 'root',
	passwd = 'hzy387hzy',
	db = 'newsInfo',
	charset = 'utf8')

dbcursor = db.cursor()
sql = 'select * from article'
dbcursor.execute(sql)
for i in range(50):
    d = dbcursor.fetchone()
    tags = jieba.analyse.extract_tags(d[2],topK = 50)
#    tags = jieba.analyse.textrank(d[2])
#    print d[2]
    print ' '.join(tags);

db.close()


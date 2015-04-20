#!usr/bin/env python
#-*- coding = utf-8 -*-

"""
1. generate key words dictionary for processing.
2. generate binary matrix. stock * keywords 
"""

import MySQLdb
import jieba
import jieba.analyse
import codecs
from sets import Set
import json

# import new dictionary for parse
jieba.load_userdict('Dict.txt')

db = MySQLdb.connect(host='localhost',
	user = 'root',
	passwd = 'hzy387hzy',
	db = 'stock',
	charset = 'utf8')

dbcursor = db.cursor()
sql = 'select name,industry from stocktable'
dbcursor.execute(sql)

result = dbcursor.fetchall()
num = len(result)

fi = open('Keywords.txt','w')
"""
for i in range(num):
    fi.write(result[i][0].encode('utf8'))
    fi.write(' ')
"""
# use dictionary to store the word. 
# remove the unesesary words and signals. 
dictionary = Set([])
for i in range(num):
    if result[i][1] is not None:
	words = result[i][1].replace(u'\u677f\u5757',u'')
        words = words.replace('_',' ')
        words = words.replace(' ','')
	words = words.replace(u'\u3000','')
        words = words.replace(u'\u3002',u'\uff0c')
        words = words.split(u'\uff0c') 
#    fi.write(result[i][1].encode('utf8'))
        for j in range(len(words)):
            dictionary.add(words[j]) 

#print dictionary
dictionary.remove(u'')
dictionary = list(dictionary)
Matrix = []
for i in range(num):
    mat = []
    for j in range(len(dictionary)):
	if result[i][1] is None:
	     mat = [0*num]
	elif dictionary[j] in result[i][1]:
	    mat.append(1)
	else:
	    mat.append(0)
 	Matrix.append(mat)

# build a dict 
stockDict = {}
for i in range (num):
    stockDict[result[i][0]]=Matrix[i]

json.dump(stockDict,open('stockMatrix.txt','w'))

# write dictionary in the txt file
for word in dictionary:
    fi.write(word.encode('utf8'))
    fi.write(' ')

db.close()
fi.close()

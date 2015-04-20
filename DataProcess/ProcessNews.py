#!usr/bin/env python
# -*- coding = utf-8 -*-

"""
usage:
    process news data from mysql.
    1. generate the frequentest key words. 
    2. find the correspoinding stock.
"""

import MySQLdb
import numpy as np
import codecs
import json

db = MySQLdb.connect(host='localhost',
	user='root',
	passwd='hzy387hzy',
	db='newsInfo',
	charset='utf8')

dbcursor = db.cursor()
sql = 'select body from article'
dbcursor.execute(sql)
result = dbcursor.fetchall()

# import the keywords dictionary in the file
filewords = codecs.open('DataProcess/Keywords.txt','r','utf-8')
words = filewords.read()
words = words.split(' ')
words.remove('')

# calculate the keywords in news and generate frequentest key words
matrix = np.zeros((1,len(words)))
for i in range(len(result)):
    for j in range(len(words)):
        numwords = result[i][0].count(words[j])

#	if words[j] in result[i][0]:
#	    numwords = 1
#	else:
#	    numwords = 0

	matrix[0][j] = matrix[0][j] + numwords
# sort the keywords matrix and print out the most frequentest words
idx = matrix.argsort()
num = len(words)
for i in range(20):
    print words[idx[0][num-1-i]],matrix[0][idx[0][num-1-i]] 

# import the matrix of stock and calculate the most relevant stock
with open('DataProcess/stockMatrix.txt') as json_file:
    stockdata = json.load(json_file)

data = np.matrix(stockdata.values())
stockname = stockdata.keys()
matrix = np.matrix(matrix)
stock = (data*matrix.getT())
idxs = stock.argsort(0) 
num = len(stockname) 
for i in range(20):
    print stockname[idxs[num-i-1][0]], stock[idxs[num-i-1][0]][0] 

# use wordtransfer at first, then use wordprocess to get dictionary for jieba

#! /usr/bin/env python
# -*- coding: utf-8 -*-


file1 = open('stockname.txt','r')
file2 = open('Dict.txt','w')

words = file1.readlines()

for word in words:
    result = word.split()
    file2.write(result[1])
    file2.write(' ')




# -*- coding: utf-8 -*-
'''
Created on 2012/04/12

@author: 0000131307
'''

import pylab

rows = 5
cols = 10
array = pylab.arange(rows*cols).reshape([rows,cols])
colNumbers = pylab.arange(cols)
rowNumbers = pylab.arange(rows)

print "array is:", array
print "******************************"
print "looping over rows"
for row in array:
    print row
print "******************************"
print "looping over cols"
for col in array.transpose():
    print col
print "******************************"
print "looping over rows with row and col information"
print "４の多重値をdictListに保存する"
dictList = []
for rowNumber, rowData in zip(rowNumbers, array):
    index = rowData % 4 == 0
    for colNumber, value in zip(colNumbers[index], rowData[index]):
        dictList.append({"row":rowNumber, "col":colNumber, "value":value})
for dct in dictList:
    print dct
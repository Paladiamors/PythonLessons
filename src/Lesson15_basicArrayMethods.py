# -*- coding: utf-8 -*-
'''
Created on 2012/04/12

@author: 0000131307
'''

import pylab

arr = pylab.array([[1,2,3,4],
                    [5,6,7,8]])
print "arr data is"
print arr
print "arr.size is:", arr.size
print "arr.shape is:", arr.shape
print "arr.min() is:", arr.min()
print "arr.max() is:", arr.max()
print "arr.flatten() is:", arr.flatten()
print "arr.sum() is:", arr.sum()
print "arr.sum(0) is:", arr.sum(0)
print "arr.sum(1) is:", arr.sum(1)
print "arr.mean() is:", arr.mean()
print "arr.mean(0) is:", arr.mean(0)
print "arr.mean(1) is:", arr.mean(1)
print "arr.std() is:", arr.std()
print "arr.std(0) is:", arr.std(0)
print "arr.std(1) is:", arr.std(1)
print "arr.reshape([4,2]) is:" 
print arr.reshape([4,2])
print "arr.transpose() is:"
print arr.transpose()
print "arr methods are:", [method for method in dir(arr) if "__" not in method]
print "use help(arr.method) to get more information"
print "help(arr.sum) is:"
help(arr.sum)
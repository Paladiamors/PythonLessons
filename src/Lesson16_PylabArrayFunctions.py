# -*- coding: utf-8 -*-

'''
Created on 2012/04/12

@author: 0000131307
'''

import pylab

print "pylabとarrayの雑多method"
print "全部では無いが、使うfunctionsを紹介する"

print "******************"
print "pylab.arangeの紹介"
print "pylab.arange(start, stop, step)"
print "pylab.arange(10):", pylab.arange(10)
print "pylab.arange(5,15):", pylab.arange(5,15)
print "pylab.arange(2,10,2):", pylab.arange(2,10,2)
print "pylab.arange(2,10,2):", pylab.arange(5.5,10.5,0.5)
print "******************"
print "pylab.randomの紹介"
print "pylab.random([5]):", pylab.random([5])
print "pylab.random([2,5]):"
print pylab.random([2,5])
print "******************"
print "pylab.ones(10) is:", pylab.ones(10)
print "pylab.ones([3,4]) is:"
print pylab.ones([3,4]) 
print "******************"
#numpy arrayのデータtypeの参照は：http://docs.scipy.org/doc/numpy/user/basics.types.html
print "データtype変換"
arr = pylab.arange(10)
print "arr is:", arr
print "pylab.bool_(arr) is:", pylab.bool_(arr)
print "pylab.float_(arr) is:", pylab.float_(arr)
print "******************"
arr = pylab.array([[3,4,5],
                   [5,6,7]])
print "data in arr is:"
print arr

print "pylab.median(arr)", pylab.median(arr)
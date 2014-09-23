# -*- coding: utf-8 -*-
'''
Created on 2012/04/12

@author: 0000131307
'''

import pylab

#array indexの参照はここ:http://www.ike-dyn.ritsumei.ac.jp/~uchida/scipy-lecture-notes/intro/numpy/numpy.html#id2

array = pylab.array(range(50*50))
array = array.reshape([50,50])
print "array is:", 
print array
print "array shape is:", array.shape

#arrayの基本座標は：
#array[row, col] or
#array[y,x]
print "*********************"
print "array[y,x] = y*50 + x or"
print "array[row,col] = row*50 + colになる "
print "array[0,10] is:", array[0,10]
print "array[1,10] is:", array[1,10]
print "array[2,10] is:", array[2,10]
print "array[2,25] is:", array[2,25]
print "*********************"
print "array slicing"
print "array[0,:] is:", array[0,:] #gets 0th row
print "array[4,:] is:", array[4,:] #gets 4th row
print "array[:,0] is:", array[:,0] #gets 0th col
print "array[:,4] is:", array[:,4] #gets 4th col
print "*********************"
print "skipping values in array"
print "array[0,::2] is:", array[0,::2] #even numbers
print "array[0,1::2] is:", array[0,1::2] #odd numbers
print "array[::2,0] is:", array[::2,0] #jump by 100 in row direction
print "array[1::2,0] is:", array[1::2,0] #jump by 100 in row direction
print "*********************"
print "getting sub-arrays"
print "array[0:2,0:2] is:"
print array[0:2,0:2]
print "array[10:12,10:12] is:"
print array[10:12,10:12] 
print "assigning values to sub arrays"
array[0:2,0:2] = 10
print "array[0:2,0:2] = 10 is:"
print array 
subArray = pylab.array([[12,13],[12,13]])
print "subArray is:"
print subArray
array[0:2,0:2] = subArray
print "array[0:2,0:2] = subArray is:"
print array
print "*********************"
print "resetting array"
array = pylab.array(range(50*50))
array = array.reshape([50,50])
print "doubling all even numbers"
evenArr = array[:,::2]
array[:,::2] = evenArr*2
print "array[:,::2] = evenArr*2"
print array
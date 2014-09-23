# -*- coding: utf-8 -*-

'''
Created on 2012/04/11

@author: 0000131307
'''

"""
numpyの紹介　→ pylabの中にnumpy moduleが入っているので、numpyのreferenceに参照が入っている:
-numpy resource:
            http://www.geocities.jp/showa_yojyo/note/python-numpy.html#array (Japanese)
            http://www.ike-dyn.ritsumei.ac.jp/~uchida/scipy-lecture-notes/intro/numpy/numpy.html
            http://www.scipy.org/Tentative_NumPy_Tutorial (English)
"""

#今回の目標、pylabのarrayの使い方
import pylab

zeros1D = pylab.zeros([5]) 
zeros2D = pylab.zeros([5,4]) 
zeros3D = pylab.zeros([5,4,2])

print "showing zeros1D"
print zeros1D
print "showing zeros2D"
print zeros2D
print "showing zeros3D"
print zeros3D
print "***********************"
print "creating a numbered list"
rangeList = range(10) #rangeをここに参照 http://www.python.jp/doc/release/library/functions.html#range
print "this is a normal list:", rangeList
print "pylab arrayに変換"
rangeArr = pylab.array(rangeList)
print "this is a pylab array:", rangeArr
print "***********************"
print "creating a 2D array"
rangeList2D = [rangeList]*3
print "2D rangeList", rangeList2D
print "converting to rangeList2D to a 2D array"
rangeArr2D = pylab.array(rangeList2D)
print rangeArr2D
print "***********************"
print "some basic array math in 1D"
array1 = pylab.array([1,2])
array2 = pylab.array([2,3])
print "array1 is:", array1
print "array2 is:", array2
print "array1+array2:", array1+array2
print "array1*2:", array1*2
print "array1/2:", array1/2
print "array1/2.0:", array1/2.0
print "array1 + 2:", array2 + 2
print "pylab.dot(array1, array2):", pylab.dot(array1, array2)

print "***********************"
print "some basic array math and matrix math in 2D"
array1 = pylab.array([[2,3],[4,5]]) 
array2 = pylab.array([[5,6],
                     [3,7]]) #このような定義でもOK
vector = pylab.array([1,2])

print "array1 is:"
print array1
print "array2 is:"
print array2
print "vector is:", vector
print "array1 + array2:"
print array1 + array2
print "array1 * array2:"
print array1 * array2
print "array1 + vector:"
print array1 + vector
print "array1 / vector:"
print array1 / vector
print "pylab.dot(array1, vector)"
print pylab.dot(array1, vector)

array1Inv = pylab.inv(array1)
print "pylab.inv(array1)"
print array1Inv
print "pylab.dot(array1, array1Inv)" 
# [[1,0],
#  [0,1]]になる
print pylab.dot(array1, array1Inv)
#pylab.crossもある
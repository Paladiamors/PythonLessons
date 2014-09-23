# -*- coding: utf-8 -*-
'''
Created on 2012/04/12

@author: 0000131307
'''

#array search and replace magic!
#これ習うのは重要

import pylab


print "*******************Array slicing*******************"
array = pylab.arange(10)
print "array is:", array
print "array[:-1] is:", array[:-1] #same as list
print "array[2:] is:", array[2:] #same as list
print "array[2:-1] is:", array[2:-1] #same as list
print "array[2:7] is:", array[2:7] #same as list
print "array[::2] is:", array[::2] #same as list
print "array[1::2] is:", array[1::2] #same as list
array[::2] = array[::2]*10
print "array[::2] = array[::2]*10:", array #for pylab (numpy) array!
array[::2] = 10
print "array[::2] = 10:", array #for pylab (numpy) array!
array[::2] = pylab.array([13,14,15,16,17])
print "array[::2] = pylab.array([13,14,15,16,17]):", array #for pylab (numpy) array!
print "*******************Search and replace with index array*******************"
randomArr = pylab.random(20)*20
randomArr = pylab.int_(randomArr)
addrArr = pylab.arange(20)
print "this is a random arr:", randomArr
print "find all values > 10"
indicies = randomArr > 10
print "indicies = randomArr > 10:", indicies #boolean array!
print "randomArr[indicies] is:", randomArr[indicies]
print "*******************"
print "find all values < 10"
indicies = randomArr < 10
print "indicies = randomArr < 10:", indicies #boolean array!
print "randomArr[indicies] is:", randomArr[indicies]
print "*******************"
print "find all values < 10 in one step"
print "randomArr[randomArr < 10] is:", randomArr[randomArr < 10]
print "*******************"
print "getting address of random < 10"
indicies = randomArr < 10
print "addrArr[indicies] is:", addrArr[indicies] 
print "randomArr is:", randomArr
print "getting values from indicies:", [randomArr[addr] for addr in addrArr[indicies]], "注意: this is a list, not numpy.array!"
print "*******************"
print "multiply all numbers > 10 by 10"
indicies = randomArr > 10
randomArr[indicies] = randomArr[indicies]*10
print "new values are:", randomArr
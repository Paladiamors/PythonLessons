# -*- coding: utf-8 -*-
'''
Created on 2012/04/11

@author: 0000131307
'''


print "basic boolean logic"
print "****************"
print "10 > 2:", 10 > 2
print "10 < 2:", 10 < 2
print "7 >= 7:", 7 >= 7
print "2 =< 2:", 2 <= 2
print "11 > 7 > 6:", 11 > 7 > 6
print "10 == 10:", 10 == 10
print "10 != 10:", 10 != 10
print "10 is 10:", 10 is 10
print "10 is 9:", 10 is 9
print "10 is not 9:", 10 is not 9
print "****************"
if []:
    print "[] is True!"
else:
    print "[] is False!"

if ["test"]:
    print '["test"] is True!'
else:
    print '["test"] is False!'

if "test" in ["this", "is", "a", "test"]:
    print 'if "test" in ["this", "is", "a", "test"] is True'
else:
    print 'if "test" in ["this", "is", "a", "test"] is False'

if "test" not in ["this", "is", "a", "test"]:
    print 'if "test" not in ["this", "is", "a", "test"] is True'
else:
    print 'if "test" not in ["this", "is", "a", "test"] is False'
print "****************"
if "":
    print '"" is True!'
else:
    print '"" is False!'

if "a string":
    print '"a string" is True!'
else:
    print '"a string" is False!'
print "****************"
    
if {}:
    print '{} is True!'
else:
    print '{} is False!'
    
if {"name": 1}:
    print '{"name": 1} is True!'
else:
    print '{"name": 1} is False!'

if "name" in {"name": 1}:
    print '"name" in {"name": 1} is True!'
else:
    print '"name" in {"name": 1} is False!'
print "****************"

#else if in python

x = 10

if x > 10:
    print "x > 10"
elif x == 10:
    print "x = 10"
else:
    print "x < 10"
    
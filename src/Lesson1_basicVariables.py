# -*- coding: utf-8 -*-
#Source codeを日本語で書くときに、上記のラインは必須

'''
Created on 2012/04/11

@author: 0000131307
'''

# this is a comment

a  = 3 
print "this is an int:", a

b = 2.0
print "this is a float:", b

c = "test string"
print "this is a string:", c

lst = [1,4,3,[3,4], "string"]
print "this is a list:", lst

tple = (2,3,4,5,3)
print "this is a tuple:", tple

st = set((2,3,4,5,3))
print "this is a set:", st

dct = {"value1":3, "value2":5 ,"value3":[2,3,4], "value4":"some value"}
print "this is a dict:", dct 

print "************************"
print "pythonのすべてのデータはobject"


## __???__の関数はこのリンクに参照：http://www.python.jp/doc/2.5/ref/customization.html
##__???__の関数はspecial関数

print "intのメンバー関数:", dir(a)
print "floatのメンバー関数:", dir(b)
print "stringのメンバー関数:", dir(c)
print "listのメンバー関数:", dir(lst)
print "tupleのメンバー関数:", dir(tple)
print "setのメンバー関数:", dir(set)
print "dictのメンバー関数:", dir(dct)


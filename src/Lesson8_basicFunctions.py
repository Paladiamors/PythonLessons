# -*- coding: utf-8 -*-
'''
Created on 2012/04/11

@author: 0000131307
'''

#Basic Functionの作り方

def adder(a,b):
    """
    adds 2 numbers
    """
    return a+b

#optionalパラメータはいつも最後
def add2Option(a,b=2):
    """
    adds 2 numbers
    bのdefaultは2
    """
    
    return a+b

#複数 optional parameters
def multiOptions(a, b=2, c=3):
    """
    adds 3 numbers
    """
    return a+b+c

def infAdder(a, *args):
    """
    無限足し算
    """
    return a + sum(args)

def infAdder2(*args):
    """
    無限足し算
    """
    return sum(args)

def multiOutput(a):
    """
    複数output
    """
    return a, a+1, a+2

def keyWord(a, **kwargs):
    """
    a = anything
    kwargs = keyword dict
    """
    print "a:", a
    print "kwargs:", kwargs
    
print "running adder:", adder(2,3)
print "running add2Option with 1 parameter:", add2Option(2)
print "running add2Option with 2 parameters:", add2Option(2,4)
print "running add2Option with named parameter:", add2Option(2,b=4)
print "running multiOptions with 1 parameter:", multiOptions(1)
print "running multiOptions with 2 parameters:", multiOptions(1,4)
print "running multiOptions with c parameter:", multiOptions(1,c=1)
print "running multiOptions:", multiOptions(1)
print "running infAdder:", infAdder(1,2,3,4,5)
print "running infAdder2:", infAdder2(1,2,3,4,5)

#a,b = inputs をしなくても配列をそのまま関数に入れられる
inputs = [2,3]
print "special unpacking:", adder(*inputs)
print "************************************"
print "すべての関数はobject,引数に設定可能"
print adder, add2Option, multiOptions, infAdder, infAdder2
a = adder
print "running a:", a(2,3)
print "************************************"
print "関数のmulti output"

print "multiOutputのoutput:", multiOutput(2)
a,b,c = multiOutput(2)
print "multiOutputのoutputを変数に保存:", a,b,c
print "************************************"
print "keyword引数の使い方"
keyWord("bob")
keyWord("bob", age=3, height=1.2, weight=66, eyeColor="blue")
keyWord("bob", **{"age":3, "height":1.2, "weight":66, "eyeColor":"blue"}) #上記の同じ、dictでも使える
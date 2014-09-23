# -*- coding: utf-8 -*-
'''
Created on 2012/04/11

@author: 0000131307
'''

#basic math
print "足し算、　引き算、　掛け算、　割り算:", 4+3, 4-3, 4*3, 4/3

print "割り算2:", 4.0/3
print "あまり:", 5 % 2
print "冪乗:", 5**2

#advanced math
import math #math libraryのimport

print "****************"
print "mathのモジュールのmember関数"
print dir(math)

#math library の関数の使え方

print "cos", math.cos(math.pi)
print "sin", math.sin(math.pi) #zeroに近い
print "tan", math.tan(math.pi) #zeroに近い
print "exp", math.exp(1)
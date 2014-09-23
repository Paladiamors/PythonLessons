# -*- coding: utf-8 -*-

'''
Created on 2012/04/11

@author: 0000131307
'''

#importing modules

print "importing testModule1"
import Lesson12_testModule1 
print "importing testModule2"
import Lesson12_testModule2

#testModule2のprint statementはimportするときに実行しない

#別moduleに同じ関数名があってもぶつからない
Lesson12_testModule1.greeting()
Lesson12_testModule2.greeting()

#もしLesson12_testModule1の名前は長すぎだったら：
#fromのkeywordを使ったら、module中身を全部再実行する
print "*******************"
from Lesson12_testModule1 import greeting
from Lesson12_testModule1 import greeting as short

print "calling greeting"
greeting()
print "calling short version of greeting"
short()

print "*******************"
print "同じmoduleを2回importすると再importしない"
import Lesson12_testModule1

print "to reload a module, use the reload command"
reload(Lesson12_testModule1)

print "*******************"
someValue = 20
print "the value of someValue is:", someValue
from Lesson12_testModule1 import someValue
print "the value of someValue is:", someValue
print "the value has been overwritten!"
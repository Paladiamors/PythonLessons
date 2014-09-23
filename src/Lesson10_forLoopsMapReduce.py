# -*- coding: utf-8 -*-
'''
Created on 2012/04/11

@author: 0000131307
'''

#for loopを基本的に配列系、iterator系objectに使う

names = ["Billy", "Anna", "Sam", "Eric", "Jennifer"] #チップ：配列系変すを複数名前を付けましょう

def simpleGreeting(name):
    return name + " says Hi!"

print "a basic loop"
output = []
for name in names: #namesの要素でloopして、loopのbodyで処理する
    output.append(simpleGreeting(name))
print output

print "output 配列無しで同じこと"
output = [simpleGreeting(name) for name in names]
print output

print "map関数で 配列無しで同じこと"
output = map(simpleGreeting, names) #mapは基本的に引数は一つの関数を使う
print output

print "***************************"
print "複数パラメータでループ"
def greet(name, greeting):
    """
    name = name string
    greeting = greeting string
    """
    
    return "%s says %s!" % (name, greeting)


print u"zipの使え方"
greetings = ["hey", "hi", "hello", "greetings", "howdy"]
print "zipの出力:", zip(names, greetings)
for name, greeting in zip(names, greetings):
    print greet(name, greeting)

#配列処理　→　他のだったら、出力配列を作って、出力する
output = []
for name, greeting in zip(names, greetings):
    output.append(greet(name, greeting))
print output

#もっと簡単方法：
output = [greet(name, greeting) for name,greeting in zip(names, greetings)]
print output
print "***************************"
print "loopでdata filtering"
numbers = [5,6,4,3,4,5,456,23,12,2234,113,4141,134,123]
print "数値filtering"
evenNumbers = [number for number in numbers if number % 2 == 0]
oddNumbers = [number for number in numbers if number % 2 == 1]
print "偶数は:", evenNumbers
print "奇数は:", oddNumbers
print "***************************"
print "reduce の使い方"
#reduceは基本的に配列を一つの値に変換する
def adder(x,y):
    return x+y
evenSum = reduce(adder, evenNumbers)
oddSum = reduce(adder, oddNumbers)
print "even and odd number totals:", evenSum, oddSum

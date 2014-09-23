# -*- coding: utf-8 -*-

'''
Created on 2012/04/11

@author: 0000131307
'''

#String処理の基礎

a = "first string"
b = "second string"
c = "a string with 2\nlines"
d = """multi
line
string"""
e = "\"quotations\"" #エスケープシーケンス参照リンク：http://www.python.jp/doc/2.5/ref/strings.html
f = r"\this is a \raw string"
g = "\this is a \raw string"
h = u"基本的にunicodeで書くときにuを付けた方はよい"

print "*************"
print a
print "*************"
print b
print "*************"
print c
print "*************"
print d
print "*************"
print e
print "*************"
print f
print "*************"
print h
print "*************"
print "stringの足し算:", a + b

a = "this is a string"
print "stringの区切り分け:", a.split()

a = "this,is,a,string"
print "カンマで区切り分け:", a.split(",")

print "カンマ区切り文字でstring join:", ",".join(["this", "is", "a", "string"])
print "スペース区切り文字でstring join:", " ".join(["this", "is", "a", "string"])
print "区切り無し文字でstring join:", "".join(["this", "is", "a", "string"])

print "string strip:", "fgabcdefg".strip("fg")
print "左string strip:", "fgabcdefg".lstrip("fg")
print "右string strip:", "fgabcdefg".rstrip("fg")

print "**************************"
#string formatting 参考リンク: http://www.python.jp/doc/2.7/library/stdtypes.html#string-formatting
print "stringの代替え:", "int %i, float %f, exponential %e, string %s" % (10, 2.34, 2123.13212, "some string")
#print 場合によって、順番で管理するのは大変な時にnamed代替えも可能
print "stringの代替え:", "int %(intVal)i, float %(floatVal)f, exponential %(expVal)e, string %(stringVal)s" % \
    {"floatVal": 2.334, "intVal": 23, "expVal": 213.123123, "stringVal": "some string"}
#代替えは複数箇所も可能,string templateも引数に保存可能
template = "%(name)s is from %(country)s and %(name)s likes %(fruit)s" 
print template % {"name": "Bob", "country":"England", "fruit": "apples"} #dictあれば、すぐtemplateに使える

print "***************************"
print "文字列検索"
a = "this is a test string"
print "'test' in '%s'?" % a, "test" in a
print "'tea' in '%s'?" % a, "tea" in a
print "aの文字数は:", len(a)






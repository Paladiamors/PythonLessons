# -*- coding: utf-8 -*-
'''
Created on 2012/04/11

@author: 0000131307
'''
#雑多os library
#参照リンクhttp://www.python.jp/doc/release/library/os.html
#Path library参照：http://www.python.jp/doc/release/library/os.path.html
#os.pathにある
import os 

filePath = "./resources/textFile.txt"
fileListPath = "./resources/writeFile.txt"
jPath  = "./resources/japanese.txt"
#openのfunction to file objectのreferenceを以下の参照リンクへ：
#http://www.python.jp/doc/release/library/functions.html#open
#http://www.python.jp/doc/release/library/stdtypes.html#bltin-file-objects

#openとfile objectのtutorialはこちらへ：
#http://www.python.jp/doc/release/tutorial/inputoutput.html#tut-files
print "opening a file for reading"
handle = open(filePath)
print "reading all data from file"
text = handle.read()
print "closing file reader"
print "this is the text in textFile.txt:"
print
print text
print
print "******************"
print "getting path list"
paths = os.listdir(".")
print "found paths are", paths

dirs = [path for path in paths if os.path.isdir(path)] #dir filter
files = [path for path in paths if not os.path.isdir(path)] #file filter

print "directories found", dirs
print "files found", files

print "print opening handle for writing"
handle = open(fileListPath, "w") #"w"のパラメータはwrite mode
print "writing list of directories to file"
handle.write(u"directories:\n")
handle.write("\n".join(dirs) + "\n")
print "writing list of files to file"
handle.write("files:\n")
handle.write("\n".join(files))
print "closing file"
handle.close()

print "fileList file and reading contents:"
handle = open(fileListPath, "r")
text = handle.read()
handle.close()
print 
print text

print "********************"
#unicode fileの読み取りと書き込みするときに別libraryは必須
#参照リンク：http://www.python.jp/doc/release/library/codecs.html
#codecs.openを見てください,基本的にopenと似てる
#codecsを使わないと、unicodeの読み取りと書き込みバケ文字になる
import codecs

print "writing japanese text to file"
handle = codecs.open(jPath, "w", encoding = "utf-8")
handle.write(u"日本語text")
handle.close()

print "reading and printing japanese text from file:"
handle = codecs.open(jPath, "r", encoding = "utf-8")
print handle.read()
handle.close() 
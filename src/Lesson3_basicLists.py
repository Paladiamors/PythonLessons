# -*- coding: utf-8 -*-

'''
Created on 2012/04/11

@author: 0000131307
'''

#PythonでListとかデータセットの処理は簡単
someList = [5,6,4,8,6,4,8]
print "this is a list:", someList

print "********************"
print "基本List operations"
print "is 4 in list?", 4 in someList
print "is 9 in list?", 9 in someList
print "sum of list:", sum(someList)
print "max of list:", max(someList)
print "min of list:", min(someList)
print "size of list:", len(someList)
print "popping list:", someList, someList.pop(), someList
print "popping list at index 0:", someList, someList.pop(0), someList
print "removing 8 from list:", someList, someList.remove(8), someList #Noneは関数からのreturnは無し
print "inserting 10 into list at index 3:", someList, someList.insert(3,10), someList
print "appending 7 to list:", someList, someList.append(7), someList
print "********************"
list1 = [4,3, "text1"]
list2 = [5,7, "text2"]
list3 = [4,3, "text1", 5,7, "text2"]
print "Intersting List operations"
print "List 足し算:", list1 + list2
print "list 掛け算:", list1*3
print "List index:", list3[2]
print "list minus index:", list3[-1]
print "List slice:", list3[1:3]
print "List slice with negative index:", list3[1:-1]
print "List slice with every 2nd element:", list3[::2]
print "List slice with every 2nd element from index1:", list3[1::2]




# -*- coding: utf-8 -*-
'''
Created on 2012/04/11

@author: 0000131307
'''

#Tupleを存在してるが、あまり使わない
tuple1 = (4,5,3,2)
tuple2 = 8,7,4,"string"
tuple3 = (4,)

print "tuple1:", tuple1
print "tuple2:", tuple2
print "tuple3:", tuple3

try: #exceptionsは今回のTutorialに対象外、robust codeを作りたいなら、習った方がいい
    tuple1[2] = 3
except:
    print "Error tupleの変換は不可"

print "setは数学のset,同じ値あったら、消される"
set1 = set((1,2,3,4,5,5))
set2 = set((5,6,7,8,9,10,10))

print "sets, たまに使う。 複写データ削除に便利"
print "set1:", set1
print "set2:", set2
print "basic set math"
print "set union:", set1.union(set2)
print "set difference:", set1.difference(set2)
print "set intersection:", set1.intersection(set1)
print "set symmetric difference:", set1.symmetric_difference(set2)


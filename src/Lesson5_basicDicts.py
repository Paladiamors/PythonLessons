# -*- coding: utf-8 -*-
'''
Created on 2012/04/11

@author: 0000131307
'''

print "dictの紹介"

"""
dictの役割は、key-valueでデータをアクセスする。
簡単なdata collectionだったらclassより簡単
"""

#peopleの名前と年齢のdict
peopleAgeDict = {"Bob": 23, "Joe": 56, "Paul":24, "Janet": 12}

print "peopleAgeDict:", peopleAgeDict
print "name, age:", "Bob", peopleAgeDict["Bob"]
print "name, age:", "Joe", peopleAgeDict["Joe"]
print "name, age:", "Janet", peopleAgeDict["Janet"]

print "peopleAgeDict keys:", peopleAgeDict.keys()
print "peopleAgeDict values:", peopleAgeDict.values()
print "peopleAgeDict items:", peopleAgeDict.items()

print "Bob in peopleAgeDict?", "Bob" in peopleAgeDict
print "Eric in peopleAgeDict?", "Eric" in peopleAgeDict

#adding new person
peopleAgeDict["Alice"] = 12
print "Adding Alice to peopleAgeDict:", peopleAgeDict
print "Removing Bob from peopleAgeDict:", peopleAgeDict.pop("Bob"), peopleAgeDict


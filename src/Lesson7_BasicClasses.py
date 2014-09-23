# -*- coding: utf-8 -*-

'''
Created on 2012/04/11

@author: 0000131307
'''

#class examples

class EmptyClass:
    """
    何もないクラス
    """
    pass

class Person:
    """
    person class, a person has a name and age
    a person can say a greeting
    """
    def __init__(self, myName, age):
        """
        myName = is a string
        age = is an int
        """
        self.myName = myName
        self.age = age

    def greeting(self, yourName):
        """
        prints a greeting
        """
        
        print "Hello! My name is %(name)s and I am %(age)i years old. Nice to meet you %(yourName)s." % {"name": self.myName, "age":self.age, "yourName":yourName}

class Woman(Person):
    """
    Personと同じが、greetingは違う
    """
    def greeting(self, yourName):
        """
        prints a greeting
        """
        
        print "Hello! My name is %(name)s and I am %(age)i years old. Nice to meet you %(yourName)s." % {"name": self.myName, "age":self.age-5, "yourName":yourName}

class RichPerson(Person):
    """
    Person with money
    """
    def __init__(self, myName, age, money):
        """
        myName = string
        age = int
        money = int
        """
        Person.__init__(self, myName, age)
        self.money = money
    
    def greeting(self, yourName):
        Person.greeting(self, yourName)
        print "I have $%i dollars!" % self.money

bob = Person("Bob", 27)    
alice = Woman("Alice", 28)
bill = RichPerson("Bill", 50, 6000)

bob.greeting("Joe")
alice.greeting("Joe")
bill.greeting("Joe")
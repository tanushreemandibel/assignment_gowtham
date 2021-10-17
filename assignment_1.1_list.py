# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:09:13 2021

@author: TANUSHREE
"""


'append'
a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)

'clear'

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

'copy'

fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)

'count'


fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)


'extend'

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)


'index'

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


'insert'


fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)


'pop'

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)


'remove '

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)


'reverse'

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)


'sort'

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
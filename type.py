#!/usr/bin/python3

a = "hello"
print(type(a))
a = 10
print(type(a))
print(hex(id(a)))
a = 15
print(hex(id(a)))


a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))


t = (1, 2, 3) #Tuples immutable

a = [1, 2] # lists are immutable

print(type(1+1))
print(type(2/3))
print(type(10/2))

import math

print(math.floor(3.15))
print(math.floor(3.99999))
print(math.floor(-3.14))
print(math.floor(-3.000000000000000000001))

a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

print(math.trunc(a/b))



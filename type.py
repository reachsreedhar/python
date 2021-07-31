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

#!/usr/bin/python3

def my_func(a, b):
  a = 5
  print(hex(id(a)))

x = 10
y = 20
print(hex(id(x)))
print(x)
my_func(x, y)
print(x)

def my_func2(a, b, c=4):
  print("a={0}, b={1}, c={2}".format(a, b, c))

my_func2(1,2)
my_func2(10,20)

def my_func3(a, b=2, c=4):
  print("a={0}, b={1}, c={2}".format(a, b, c))

my_func3(c=30, b=20, a=10)

my_func3(10, c=30, b=20)
my_func3(20)

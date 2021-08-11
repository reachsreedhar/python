#!/usr/bin/python3

print(callable(print))

result = print('hello')
print(result)

l = [1,2,3]

print(callable(l.append))

s = 'abc'
print(callable(s.upper))
result = s.upper()
print(result)

from decimal import Decimal

print(callable(Decimal))

class MyClass:
  def __init__(self, x=0):
    print('initializing...')
    self.counter = x

  def __call__(self, x=1):
    print('updating counter...')
    self.counter += x

print(callable(MyClass))

a = MyClass(100)

print(callable(a))

b = MyClass()

MyClass.__call__(b, 10)

print(callable(b))

b()

print(b.counter)

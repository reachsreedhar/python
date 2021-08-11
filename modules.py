#!/usr/bin/python3

def func():
  print('test')
  a = 10
  b = 10
  print(locals())
print(globals())

f = globals()['func']

f()

print(locals())

import math
print(math)
import fractions
print(fractions)
print(type(fractions))
print(type(math))

import sys

#print(sys.modules)

import types
print(isinstance(math, types.ModuleType))

mod = types.ModuleType('test', 'This is a test module')

from types import ModuleType
print(isinstance(mod, types.ModuleType))

mod.hello = lambda: 'Hello!'

print('hello' in globals())
hello()

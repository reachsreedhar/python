#!/usr/bin/python3

x = 0.1

x = 0.1 + 0.1 + 0.1
y = 0.3

print(x == y)
print(format(x, '.25f'))
print(format(y, '.25f'))

print(round(x, 3) == round(y, 3))

x = 10000.01
y = 10000.02

delta = y - x

from math import isclose 
from math import trunc
import math

#help(isclose)
print(isclose(x, y))
isclose(x, y, rel_tol = 0.01, abs_tol = 0.01)
print(math.trunc(10.4))

print(math.floor(10.4))
print(math.floor(-10.4))

print(math.ceil(10.4))
print(math.ceil(-10.4))

print('round')
print(round(10.5))
print(round(10.5, 0))
print(round(10.5, 1))
print(round(10.5, 2))
print(round(10.3))
print(round(10.6))

print(round(1.8888, 3))
print(round(1.8888, 2))
print(round(1.8888, 1))
print(round(1.8888, 0))

print(round(888.88, 1))
print(round(888.88, 0))
print(round(888.88, -1))
print(round(888.88, -2))
print(round(888.88, -3))
print(round(888.88, -4))
print(round(7010, -4))

print(round(1.25, 1))
print(round(1.35, 1))

print(round(-1.25, 1))
print(round(-1.35, 1))

def _round(x):
  from math import fabs, copysign
  return int(x + 0.5 * copysign(1, x))

print(round(1.5))
print(_round(1.5))
print(round(2.5))
print(_round(2.5))

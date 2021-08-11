#!/usr/bin/python3

import operator

print(dir(operator))

print(operator.add(1, 2))
print(operator.mul(1, 2))
print(operator.truediv(3, 2))
print(operator.floordiv(13, 2)) # 13 // 2

from functools import reduce

print(reduce(lambda x, y: x*y, [1,2,3,4]))
print(reduce(operator.mul, [1,2,3,4]))

print(operator.lt(10, 3))

from operator import is_

print(is_('abc','def'))
print(is_('abc','abc'))
print(operator.truth([]))
print(operator.truth([1]))

my_list = [1,2,3,4]
print(my_list[1])

print(operator.getitem(my_list, 1))

print(my_list)
del my_list[3]
print(my_list)

operator.setitem(my_list, 1, 100)
print(my_list)
operator.delitem(my_list, 2)
print(my_list)

f = operator.itemgetter(2)
print(type(f))
my_list = [1,2,3,4]
print(f(my_list))

s = 'python'
print(f(s))

f = operator.itemgetter(2,3)
my_list = [1,2,3,4]
print(f(my_list))

print(f('sreedhar'))

class MyClass:
  def __init__(self):
    self.a = 10
    self.b = 20
    self.c = 30

  def test(self):
    print('test method running...')

obj = MyClass()

print(obj.a)
print(obj.b)
obj.test()

prop_a = operator.attrgetter('a')

print(prop_a(obj))

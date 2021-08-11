#!/usr/bin/python3

# sorted, map, filter, zip
# map(func, *iterables)

l = [2,3,4]
l2 = [10,20,30]
l3 = [100,200,300]
def sq(x):
  return x**2

def add(x, y):
  return x + y

print(list(map(sq, l)))
print(list(map(add, l, l2)))
print(list(map(lambda x, y: x+y, l, l2)))
print(list(map(lambda x, y, z: x+y+z, l, l2, l3)))

# filter(func, iterable)

l = [0, 1, 2, 3, 4]
print(list(filter(None, l)))

def is_even(n):
  return n % 2 == 0

print(list(filter(is_even, l)))
print(list(filter(lambda n: n % 2 == 0, l)))

# zip (*iterables)

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'
print(list(zip(l1, l2)))
print(list(zip(l1, l2, l3)))
l1 = range(100)
l2 = 'abcd'
print(list(zip(l1, l2)))

# List Comprehension - Alternative to map
# [<expression> for <varname> in <iterable>]
l4 = [100,200,300]
l5 = [1,2,3]
print([x**2 for x in l4])
print(list(map(sq, l4)))
print([x + y for x, y in zip(l4, l5)])

# List comprehension alternative to filter
# [<expr> for <var> in <iterable> if <expr 2>]
l = [1, 2, 3, 4]
print(list(filter(lambda n: n % 2 == 0, l)))
r = [x for x in l if x % 2 == 0]
print(r)

# Combining map and filter
l = range(10)

r = list(filter(lambda y: y < 25, map(lambda x: x**2, l)))
print(r)
r = [x**2 for x in range(10) if x**2 < 25]
print(r)

# coding
def fact(n):
  return 1 if n< 2 else n * fact(n-1)

print(fact(3))
print(fact(4))

print(list(map(fact, range(6))))

l1 = [1,2,3,4,5]
l2 = [10,20,30]

results = list(map(lambda x, y: x + y, l1, l2))
print(results)

result = list(filter(lambda x: x % 3 == 0, range(25)))
print(result)

l2 = [10, 20, 30, 40]
l3='python'

results = list(zip(l1, l2, l3))
for x in results:
  print(x)

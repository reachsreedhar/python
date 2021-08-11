#!/usr/bin/python3

def my_func(a, b, c):
  print(a, b, c)

my_func(10,20,30)
f = lambda b, c: my_func(10, b, c)

from functools import partial

#def f(x,y):
  #return my_func(10, x, y)

# below is same above function f
f = partial(my_func, 10)

f(20, 30)

def pow(base, exponent):
  return base ** exponent

square = partial(pow, exponent = 2)
cube = partial(pow, exponent = 3)

print(square(5))
print(square(5, exponent=3))
print(cube(5))

def my_func2(a, b, *args, k1, k2, **kwargs):
  print(a, b, args, k1, k2, kwargs)

my_func2(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)

#def f2(x, *vars, kw, **kwvars):
  #return my_func2(10, x, *vars, k1='a', k2=kw, **kwvars)

# Below is same above function f2
f2 = partial(my_func2, 10, k1='a')
  
f2(20, 100, 200, k2='b', k3=1000, k4=2000)


def my_func3(a, b):
  print(a, b)

a = [1,2]

f3 = partial(my_func3, a)
f3(100)
a.append(3)
print(a)
f3(100)

origin = (0,0)
l = [(1,1), (0,2), (-3,2), (0,0), (10,10)]
dist2 = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2

print(dist2((1,1), origin))

f = partial(dist2, origin)
print(f((1,1)))

print(sorted(l, key=f))

f = lambda x: dist2(origin, x)
print(sorted(l, key=f))

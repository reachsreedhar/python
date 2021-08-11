#!/usr/bin/python3

def sq(i):
  return i**2

def apply_func(fn, *args, **kwargs):
  return fn(*args, **kwargs)

print(apply_func(sq, 3))
print(apply_func(lambda x: x**2, 3))
print(apply_func(lambda x, y: x+y, 1, 3))
print(apply_func(lambda x, *, y: x+y, 1, y=20))
print(apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))
print(apply_func(sum, (1, 2, 3, 4, 5, 6, 7)))


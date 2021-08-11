#!/usr/bin/python3

#  **kwargs -> dictionary

def func1(**others):
  print(others)

func1(a=1, b=2, c=3)

def func2(*args, **kwargs):
  print(args)
  print(kwargs)

func2(1, 2, x=100, y=200)

def func3(a, b, *, d, **kwargs):
  print(a)
  print(b)
  print(kwargs)

print('here')
func3(1, 2, x=100, y=200, d=20)

def func4(a, b, **kwargs):
  print(a, sep='|')
  print(b, sep='|')
  print(kwargs, sep='|')

func4(1, 2, x=100, y=200)

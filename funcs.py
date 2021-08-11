#!/usr/bin/python3

def func(a, b, *args):
  print(a, b, args)


func(1, 2, 'x', 'y', 'z')

def func2(a, b=2, c=3, *args):
  print(a, b, c, args)


func2(1, 4, 3, 'x','y','z')

def func3(a, b=5, *args, c=3, d):
  print(a, b, args, c, d)

func3(10, 20, 'x', 'y','z', c=4, d=1)

def func4(a, b, *args, c=10, d=20, **kwargs):
  print(a, b, args, c, d, kwargs)

func4(1, 2, 'x','y','z', c=100, d=200, x=0.1, y=0.2)

print(1, 2, 3, sep='-', end=' *** ')
print(1, 2, 3)

def calc_hi_lo_avg(*args, log_to_console=False):
  hi = int(bool(args)) and max(args)
  lo = int(bool(args)) and min(args)

  avg = (hi + lo)/2
  if log_to_console:
    print("hi = {0}, low={1}, avg={2}".format(hi, lo, avg))
  return avg

is_debug=True
avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=is_debug)

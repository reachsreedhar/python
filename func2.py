#!/usr/bin/python3
a, b, *c = 10, 20, 'a','b'
print(a, b, c)

def func1(a, b, *args):
  print(a)
  print(b)
  print(args)

func1(10, 20, 1, 2, 3)

def avg(*args):
  count=len(args)
  total = sum(args)
  #if count > 0:
    #a = total/count
  #else:
    #a = 0
  #return a
  return count and total/count

print(avg())
print(avg(10, 20))
print(avg(10, 20, 30, 40, 50))

def func2(a, b, *args):
  print(a)
  print(b)
  print(args)

print('here')
l = [10, 20, 30, 40]
func2(*l)

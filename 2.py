#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys

print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2**1000))

def calc(a):
  for i in range(10000000):
    a*2

import time

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print('1 : ',end-start)

start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print('2 : ',end-start)

start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print('3 : ',end-start)

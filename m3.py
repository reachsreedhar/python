#!/usr/bin/python3
from decimal import Decimal

import sys

a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))

import time

def run_float(n=1):
  for i in range(n):
    a = 3.1415

def run_decimal(n=1):
  for i in range(n):
    a = Decimal('3.1415')

n = 10000000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float : ', end - start)
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal : ', end - start)

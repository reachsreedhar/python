#!/usr/bin/python3

# Also called accumulators, aggregators or folding functions

l = [5,8,6,10,9]

def _reduce(fn, sequence):
  result = sequence[0]
  for a in sequence[1:]:
    result = fn(result, a)
  return result

r = _reduce(lambda a, b: a if a > b else b, l)
print(r)
r = _reduce(lambda a, b: a if a < b else b, l)
print(r)
r = _reduce(lambda a, b: a + b, l)
print(r)

from functools import reduce

r = reduce(lambda a, b: a if a>b else b, l)
print(r)
r = reduce(lambda a, b: a if a<b else b, l)
print(r)
r = reduce(lambda a, b: a + b, l)
print(r)

print(reduce(lambda a, b: a if a < b else b, 'python'))

print(min(l))
print(max(l))
print(any(l))
print(sum(l))
print(all(l))

l = [0, '', None, 100]
print(any(l))
print(all(l))

s = [True, 0 ,1, None]

print(reduce(lambda a, b: bool(a) and bool(b), s))

l = [1,2,3,4]
l = range(1,5)
r = reduce(lambda a, b: a * b, l)
print(l)
print(r)

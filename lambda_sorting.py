#!/usr/bin/python3

l = [1,4,3,6,7,8]

print(l)
print(sorted(l))

l = ['c', 'B', 'D', 'a']
print(l)
print(sorted(l))
print(ord('a'))
print(ord('A'))
print(sorted(l, key=lambda s: s.upper()))

d = {'def': 300, 'abc': 300, 'ghi': 100}
print(d)
print(sorted(d))
print(sorted(d, key=lambda e: d[e]))

def dist_sq(x):
  return (x.real)**2 + (x.imag)**2

print(dist_sq(1+1j))

l = [3+3j, 1-1j, 0, 3+0j]

print(sorted(l, key=dist_sq))

print(sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2))

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(l)
print(sorted(l))
print(sorted(l, key=lambda s: s[-1]))

l = ['Idle', 'Cleese', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(l)
print(sorted(l))
print(sorted(l, key=lambda s: s[-1]))

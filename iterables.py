#!/usr/bin/python3

t = 1,

print(t)

l = [1,2,3]
t = (1,2,3)
s = {1,2,3}

print(l) # list
print(t) # tuple
print(s) # set

a = 10
b = 20

print(a, b)
a, b = b, a

print(a, b)

s = {'p','y','t','h','o','n'}
l = ('p','y','t','h','o','n')

print(s)
print(l)

a = (1,2,3)
print(type(a))
a = [1,2,3]
print(type(a))
a = {1,2,3}
print(type(a))

a, b, c = [1, 'a', 3.14]
print(a, b, c)

a, b = (1,2)
print(a, b)

a, b = 10, 20
print(type(a))
print(type((1,2)))


for e in 'xyz':
  print(e)
print(type('xyz'))
s = {'p','y','t','h','o','n'}
print(s)

for e in s:
  print(e)

print('here')
dic = {'a':1, 'b':2, 'c':3}
for e in dic:
  print(e)

print(dic.values)

for t in dic.items():
  a,b = t
  #print(t)
  print(a, b)

l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:2]
c = l[1:]

print(a)
print(b)
print(c)

x, *y = l
print(x)
print(y)

a, b, *c = 'sreedhar'
print(a)
print(b)
print(c)
a, b, *c, d = 'sreedhara'
print(a)
print(b)
print(c)
print(d)
l1 = [1,2,3]
l2 = [4,5,6]
l = [*l1, *l2]
print(l1)
print(l2)
print(l)

l2 = 'xyz'
l = [*l1, *l2]
print(l1)
print(l2)
print(l)

# Types such as sets and dictionaries have NO ORDERING
s = {10, -99, 3, 'd'}
print(s)
d1 = {'p':1, 'y':2}
d2 = {'t':3, 'h':4}
d3 = {'h':5, 'o':6, 'n':7}

l = [*d1, *d2, *d3]
s = {*d1, *d2, *d3}
d = {**d1, **d2, **d3}

print(l)
print(s)
print(d)

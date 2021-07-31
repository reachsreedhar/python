#!/usr/bin/python3

def process(s):
  print('Initial s # = {0}'.format(id(s)))
  s = s + ' world'
  print('Final s # = {0}'.format(id(s)))
  return s

def process2(lst):
  print('Initial lst # = {0}'.format(id(lst)))
  lst.append(100)
  print('Final lst # = {0}'.format(id(lst)))


def modify_tuple(t):
  print('Initial t # = {0}'.format(id(t)))
  t[0].append(100)
  print('Final t # = {0}'.format(id(t)))


t = ([1, 2], [3,4])

print(t)

my_var = 'hello'
print('my_var # = {0}'.format(id(my_var)))
print(process(my_var))

my_list = [1, 2, 3]
print('my_list # = {0}'.format(id(my_list)))
print(process2(my_list))
print(my_list)

my_tuple = ([1,2], 'a')
print('before my_tuple : {0}'.format(my_tuple))
print('my_tuple # = {0}'.format(id(my_tuple)))
print(modify_tuple(my_tuple))
print('after my_tuple : {0}'.format(my_tuple))

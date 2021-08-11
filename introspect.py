#!/usr/bin/python3

# TODO: Fix this function
# currnently does nothing
def my_func(a: "mandatory positional", 
            b: "optional positional" = 1, 
            c=2, 
            *args: "add extra positional here", 
            kw1, 
            kw2=100, 
            kw3=200, 
            **kwargs: "provide extra kw-only here") -> "does nothing" :
  """This function does nothing but does have various parameters
     and annotations.
  """
  i = 10
  j = 20
  x = i + j

my_func(1, kw1='a')

print(my_func.__doc__)
print(my_func.__annotations__)

my_func.short_description = "This is a function that does nothing much"

print(my_func.short_description)

print(dir(my_func))
print(my_func.__name__)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)

import inspect

from inspect import isfunction, ismethod, isroutine

a = 10
print(isfunction(a))
print(isfunction(my_func))
print(ismethod(my_func))

class MyClass:
  def f(self):
    pass

print(ismethod(MyClass.f))
print(isfunction(MyClass.f))

myobj = MyClass()
print(ismethod(myobj.f))
print(isfunction(myobj.f))
print(isroutine(myobj.f))

print(inspect.getsource(my_func))

import math

print(inspect.getmodule(my_func))
print(inspect.getmodule(math.sin))

print(inspect.getcomments(my_func))

print(inspect.signature(my_func))

print(my_func.__annotations__)

print(inspect.signature(my_func).return_annotation)

sig = inspect.signature(my_func)

for param in sig.parameters.values():
  # print(dir(v))
  print('Name :', param.name)
  print('Default :', param.default)
  print('Annotation :', param.annotation)
  print('Kind :', param.kind)

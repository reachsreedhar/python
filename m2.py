#!/usr/bin/python3

import decimal
from decimal import Decimal

print(decimal.getcontext())
gctx = decimal.getcontext()

with decimal.localcontext() as ctx:
  ctx.prec = 2
  ctx.rounding = decimal.ROUND_HALF_UP
  print(decimal.getcontext())
  print(gctx)
  x = Decimal('1.25')
  y = Decimal('1.35')
  print(round(x, 1))
  print(round(y, 1))

print(round(x, 1))
print(round(y, 1))
print(Decimal(0.1))
a = Decimal((1, (3,1,4,1,5), -4))
print(a)

#decimal.getcontext().prec = 2
a = Decimal('0.12345')
b = Decimal('0.12345')
c = a + b
print(a, b, c)

with decimal.localcontext() as ctx:
  ctx.prec = 2
  c = a + b
  print(a, b, c)

#help(Decimal)

print(Decimal('0.1'))
print(Decimal(0.1))

decimal.getcontext().prec = 2

a = Decimal('0.12345')
b = Decimal('0.12345')

c = a + b

print(a, b, c)

print ("here")
#n = d * (n // d) + (n % d)
x = 10
y = 3
print(x // y, x % y)
print(divmod(x, y))
print(x == (y * (x//y) + (x%y)))

x = Decimal(10)
y = Decimal(3)
print(x // y, x % y)
print(divmod(x, y))
print(x == (y * (x//y) + (x%y)))

x = Decimal(-10)
y = Decimal(-3)
print(x // y, x % y)
print(divmod(x, y))
print(x == (y * (x//y) + (x%y)))

decimal.getcontext().prec = 28

a = Decimal('1.5')
print(a)
print(a.ln())
print(a.exp())
print(a.sqrt())

import math
print(math.sqrt(a))

a = Decimal('2')
print(a)
print(a.ln())
print(a.exp())
print(a.sqrt())

import math
print(math.sqrt(a))

x = 2
x_dec = Decimal(2)

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)


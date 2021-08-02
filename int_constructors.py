#!/usr/bin/python3

print(int("1010", 2))
print(int("a12f", base=16))
print(int("534", base=8))
print(bin(10))
print(oct(20))
print(hex(40))
a = 0b1010
print(a)
b = 0o40
print(b)
c = 0x100
print(c)

def encode(digits, digit_map):
  if max(digits) >= len(digit_map):
    raise ValueError("digit_map is not long enough to encode the digits")
  #encoding = ''
  #for d in digits:
    #encoding += digit_map[d]
  #return encoding  
  return ''.join([digit_map[d] for d in digits])

def from_base10(n, b):
  if n == 0:
    return [0]
  if b < 2:
    raise ValueError('Base b must be >= 2')
  if n < 0:
    raise ValueError('Number n must be >= 0')
  digits = []
  while n > 0:
    #m = n % b
    #n = n // b
    #m, n = n % b, n//b
    n, m = divmod(n, b)
    digits.insert(0, m)
  #edigits = encoding(digits)
  return digits
  
def rebase_from10(number, base):
  digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if base < 2 or base > 36:
    raise ValueError('Invalid base: 2 <= base <= 36')
  sign = -1 if number < 0 else 1
  number *= sign

  digits = from_base10(number, base)
  encoding = encode(digits, digit_map)
  if sign == -1:
    encoding = '-' + encoding
  return encoding


print(from_base10(1000, 11))
print(from_base10(0, 11))

import fractions

a = fractions.Fraction(22, 7)

print(a)

print(encode([11, 15, 15], '01234567889ABCDEF'))

e = rebase_from10(10, 2)
print(e)
e = rebase_from10(160, 16)
print(e)

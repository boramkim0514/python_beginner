Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> print( " Python 강좌 006 - 진수 다루기 ")
 Python 강좌 006 - 진수 다루기 
>>> 
>>> print(" 파이썬의 2진수, 8진수, 16진수 ")
 파이썬의 2진수, 8진수, 16진수 
>>> 
>>> 
>>> 10
10
>>> 
>>> bin(10)
'0b1010'
>>> 
>>> oct(10)
'0o12'
>>> 
>>> hex(10)
'0xa'
>>> 
>>> 
>>> a = 20
>>> 
>>> bin(a), oct(a), hex(a)
('0b10100', '0o24', '0x14')
>>> 
>>> 
>>> a = 12
>>> b = bin(12)
>>> c = oct(12)
>>> d = hex(12)
>>> 
>>> print(a, b, c, d)
12 0b1100 0o14 0xc
>>> 
>>> print(" 10진수 = %ㅇ, 2 진수 = %s, 8진수 = %s, 16진수  = %s " % (a, b, c, d))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(" 10진수 = %ㅇ, 2 진수 = %s, 8진수 = %s, 16진수  = %s " % (a, b, c, d))
ValueError: unsupported format character '?' (0x3147) at index 9
>>> print(" 10진수 = %0, 2 진수 = %s, 8진수 = %s, 16진수  = %s " % (a, b, c, d))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(" 10진수 = %0, 2 진수 = %s, 8진수 = %s, 16진수  = %s " % (a, b, c, d))
ValueError: unsupported format character ',' (0x2c) at index 10
>>> print(" 10진수 = %d, 2 진수 = %s, 8진수 = %s, 16진수  = %s " % (a, b, c, d))
 10진수 = 12, 2 진수 = 0b1100, 8진수 = 0o14, 16진수  = 0xc 
>>> File "<pyshell#29>", line 1, in <module>
SyntaxError: invalid syntax
>>> a = 10
>>> 
>>> b = 'Ob1010'
>>> 
>>> c = '
SyntaxError: EOL while scanning string literal
>>> c = 'Oo12'
>>> 
>>> d = 'Oxa'
>>> 
>>> a, b, c, d
(10, 'Ob1010', 'Oo12', 'Oxa')
>>> 
>>> 
>>> type
<class 'type'>
9
>>> type(a), type(b), type(c), type(d)
(<class 'int'>, <class 'str'>, <class 'str'>, <class 'str'>)
>>> 
>>> for i in range(0, 11):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
>>> 
>>> 
>>> for i in range(0, 11):
res = 2 ** i-1
print(" %4d ==> [%-15s] " % (res, bin(res))
      
SyntaxError: expected an indented block
>>> 
>>> for i in range(0, 11):
res = 2 ** i-1
print(" %4d ==> [%-15s] " % (res, bin(res))
      
SyntaxError: expected an indented block
>>> 
>>> 
>>> 
>>> for i in range(0, 11):
res = 2 ** i-1
print(" %4d ==> [%-15s] " % (res, bin(res))
      
SyntaxError: expected an indented block
>>> 
>>> for i in range(0, 11):
res = 2 ** i-1
print(" %4d ==> [%-15s] " % (res, bin(res)))
SyntaxError: expected an indented block
>>> for i in range(0, 11):
	res = 2 ** i-1
	print(" %4d ==> [%-15s] " % (res, bin(res)))

	
    0 ==> [0b0            ] 
    1 ==> [0b1            ] 
    3 ==> [0b11           ] 
    7 ==> [0b111          ] 
   15 ==> [0b1111         ] 
   31 ==> [0b11111        ] 
   63 ==> [0b111111       ] 
  127 ==> [0b1111111      ] 
  255 ==> [0b11111111     ] 
  511 ==> [0b111111111    ] 
 1023 ==> [0b1111111111   ] 
>>> 
>>> 
>>> for i in range(0, 11):
	res = 2 ** 1
	print(" 2 ^ %2d ==> [%5d] " % (i, res)))
	
SyntaxError: unmatched ')'
>>> 
>>> for i in range(0, 11):
	res = 2 ** 1
	print(" 2 ^ %2d ==> [%5d] " % (i, (res)))

	
 2 ^  0 ==> [    2] 
 2 ^  1 ==> [    2] 
 2 ^  2 ==> [    2] 
 2 ^  3 ==> [    2] 
 2 ^  4 ==> [    2] 
 2 ^  5 ==> [    2] 
 2 ^  6 ==> [    2] 
 2 ^  7 ==> [    2] 
 2 ^  8 ==> [    2] 
 2 ^  9 ==> [    2] 
 2 ^ 10 ==> [    2] 
>>> 
>>> 
>>> for i in range(0, 11):
	res = 2 ** i
	print(" 2 ^ %2d ==> [%15s] " % (i, bin(res)))

	
 2 ^  0 ==> [            0b1] 
 2 ^  1 ==> [           0b10] 
 2 ^  2 ==> [          0b100] 
 2 ^  3 ==> [         0b1000] 
 2 ^  4 ==> [        0b10000] 
 2 ^  5 ==> [       0b100000] 
 2 ^  6 ==> [      0b1000000] 
 2 ^  7 ==> [     0b10000000] 
 2 ^  8 ==> [    0b100000000] 
 2 ^  9 ==> [   0b1000000000] 
 2 ^ 10 ==> [  0b10000000000] 
>>> 
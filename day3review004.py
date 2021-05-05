Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(" 파이썬(python) - 실수를 공부합니다. ")
 파이썬(python) - 실수를 공부합니다. 
>>> 
>>> 3.14
3.14
>>> 
>>> type(3.14)
<class 'float'>
>>> 
>>> type(10/3)
<class 'float'>
>>> 
>>> 10 / 3
3.3333333333333335
>>> 
>>> a = 10 / 3
>>> 
>>> print(a)
3.3333333333333335
>>> 
>>> print(" a = %f \n" % a )
 a = 3.333333 

>>> 
>>> print(" a = %.20f \n" % a )
 a = 3.33333333333333348136 

>>> print(" a = %.2f \n" % a )
 a = 3.33 

>>> 
>>> print(" a = %.1f \n % a )
      
SyntaxError: EOL while scanning string literal
>>> print(" a = %.2f \n" % a )
 a = 3.33 

>>> print(" a = %.1f \n" % a )
 a = 3.3 

>>> f = 5.15 - 5.05)
SyntaxError: unmatched ')'
>>> f = 5.15 - 5.05
>>> f
0.10000000000000053
>>> 
>>> sum = 0.0
>>> 
>>> for i in range(100):
	sum = sum + 1.7

	
>>> print(sum)
169.99999999999986
>>> 
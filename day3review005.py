Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print(" 파이썬에서 문자열(str) 코딩 ")
 파이썬에서 문자열(str) 코딩 
>>> 
>>> korea
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    korea
NameError: name 'korea' is not defined
>>> 'korea'
'korea'
>>> 
>>> "korea"
'korea'
>>> 
>>> print('korea')
korea
>>> 
>>> print("korea")
korea
>>> 
>>> 
>>> 
>>> type("ace")
<class 'str'>
>>> 
>>> a = "ace"
>>> 
>>> type(a)
<class 'str'>
>>> 
>>> a
'ace'
>>> 
>>> a[0]
'a'
>>> a[1]
'c'
>>> a[2]
'e'
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a[3]
IndexError: string index out of range
>>> 
>>> 
>>> 
>>> k = 'king'
>>> 
>>> k
'king'
>>> k + 2
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    k + 2
TypeError: can only concatenate str (not "int") to str
>>> k * 2
'kingking'
>>> K * 3
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    K * 3
NameError: name 'K' is not defined
>>> k * 3
'kingkingking'
>>> 
>>> 
>>> p = 'pine'
>>> a = 'apple'
>>> p
'pine'
>>> a
'apple'
>>> p + a
'pineapple'
>>> 
>>> t
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> t = p + a
>>> 
>>> t
'pineapple'
>>> print(t)
pineapple
>>> 
>>> 
>>> p = 'programming'
>>> 
>>> p
'programming'
>>> 
>>> len(p)
11
>>> 
>>> p[:2]
'pr'
>>> 
>>> p[:3]
'pro'
>>> 
>>> p[0:3]
'pro'
>>> 
>>> p[0:5]
'progr'
>>> 
>>> p[8:]
'ing'
>>> 
>>> p[5:]
'amming'
>>> 
>>> p[4:7]
'ram'
>>> 
>>> 
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 3.45
>>> num
3.45
>>> num = 16
>>> math.sqrt(num)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    math.sqrt(num)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(num)
4.0
>>> num = 3.45
>>> math.ceil(num)
4
>>> math.floor(num)
3
>>> 
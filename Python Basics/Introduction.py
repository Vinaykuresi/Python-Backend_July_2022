Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> initial = 34
>>> left = 13
>>> arrived = 34
>>> current = initial - left + arrived
>>> current
55
>>> initial
34
>>> 1+"1"
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    1+"1"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> num = 20
>>> def add():
	num1 = 30
	print("Sum of Numbers : ", num+num1)

	
>>> def sub():
	num2 = 10
	print("Sub of Numbers : ", num-num2)

	
>>> add()
Sum of Numbers :  50
>>> sub()
Sub of Numbers :  10
>>> print("Sum of Numbers : ", num+num1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print("Sum of Numbers : ", num+num1)
NameError: name 'num1' is not defined
>>> print("Sub of Numbers : ", num-num2)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print("Sub of Numbers : ", num-num2)
NameError: name 'num2' is not defined
>>> "1"-"1"
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    "1"-"1"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> "1"*"1"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    "1"*"1"
TypeError: can't multiply sequence by non-int of type 'str'
>>> def add():
	global num1
	num = 30
	print("Sum of Numbers : ", num+num1)

	
>>> add()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    add()
  File "<pyshell#23>", line 4, in add
    print("Sum of Numbers : ", num+num1)
NameError: name 'num1' is not defined
>>> def add():
	global num1
	num1 = 30
	print("Sum of Numbers : ", num+num1)

	
>>> add()
Sum of Numbers :  50
>>> print("Sum of Numbers : ", num+num1)
Sum of Numbers :  50
>>> num1
30
>>> type(num1)
<class 'int'>
>>> num1 = "Vinay"
>>> num1
'Vinay'
>>> type(num1)
<class 'str'>
>>> 
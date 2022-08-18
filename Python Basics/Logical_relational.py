Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 20
>>> (num*True)+30 >= (10*2) >= (((False*True)+37) - 26)
True
>>> 50 >= 55 >= 11
False
>>> # false >= 11
>>> 0 >= 11
False
>>> 50 >= (55 >= 11)
True
>>> num1 = 30
>>> num2 = 32
>>> num3 = 40
>>> 
>>> num1 += num2
>>> # num1 = num1 + num2
>>> num1
62
>>> num2 /= 4
>>> num2
8.0
>>> # num2 = num2 / 4
>>> num3 %= num2
>>> num3
0.0
>>> # num3 = num3 % num2
>>> num3
0.0
>>> num3 *=(True+1)
>>> num3
0.0
>>> num2 /=(True+num3)*num1
>>> num2
0.12903225806451613
>>> (10-9)*False+True and (32/4*True or 40%5)
8.0
>>> (32/4*True or 40%5)
8.0
>>> (10-9)*False+True
1
>>> 1 and 8
8
>>> 9 and 8
8
>>> (10>9)>False and (True or False)
True
>>> 1 + 1.0
2.0
>>> 1 + int(1.0)
2
>>> type(2)
<class 'int'>
>>> str(2)
'2'
>>> int('2')
2
>>> type(str(2))
<class 'str'>
>>> type(int('2'))
<class 'int'>
>>> 1+"1"
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    1+"1"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> "1"+"1"
'11'
>>> "Vinay "+"Kumar"
'Vinay Kumar'
>>> 
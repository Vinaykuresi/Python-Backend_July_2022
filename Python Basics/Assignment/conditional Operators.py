Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 10
>>> num2 = 20
>>> num3 = 30
>>> 
>>> (((num2/num3) > 1) or (13-12)<12/3) and ((12+13)%5+10)-230
-220
>>> ((num2/num3) > 1)
False
>>> (13-12)<12/3)
SyntaxError: unmatched ')'
>>> (13-12)<12/3))
SyntaxError: unmatched ')'
>>> (13-12)<12/3
True
>>> (((num2/num3) > 1) or (13-12)<12/3)
True
>>> ((12+13)%5+10)-230
-220
>>> ((12+(num += 12))%5+10)-230
SyntaxError: invalid syntax
>>> ((12+13)%5+10) < 230*num
True
>>> (((num2/num3) > 1) or (13-12)<12/3) and ((12+13)%5+10) < 230*num
True
>>> 
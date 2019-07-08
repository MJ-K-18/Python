Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> 
>>> type a
SyntaxError: invalid syntax
>>> type( a )
<class 'int'>
>>> 
>>> 
>>> b = 3.141592
>>> 
>>> type( b )
<class 'float'>
>>> 
>>> c = True
>>> type ( c )
<class 'bool'>
>>> 
'
>>> d = b'10'
>>> type( d )
<class 'bytes'>
>>> 
>>> 
>>> id( a )
140704974136240
>>> id( b )
2520379733840
>>> id( c )
140704973617488
>>> id( d )
2520390216080
>>> 
>>> 
>>> a
10
>>> id( a )
140704974136240
>>> a = 20
>>> a
20
>>> id( a )
140704974136560
>>> 
>>> b =10
>>> id( b )
140704974136240
>>> type( b )
<class 'int'>
>>> b= = 30
SyntaxError: invalid syntax
>>> b = 30
>>> b
30
>>> id( 30 )
140704974136880
>>> 
>>> 
>>> import sys
>>> sys.getrefcount( a )
35
>>> sys.getrefcount( b )
20
>>> a = 100
>>> b = a
>>> a
100
>>> b
100
>>> id(a )
140704974139120
>>> id( b 0
    
SyntaxError: invalid syntax
>>> id (b )
140704974139120
>>> 
>>> 
>>> 
>>> 
>>> a =1
>>> a< 0
False
>>> a>0
True
>>> True + True
2
>>> True + False
1
>>> boll( 3 )
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    boll( 3 )
NameError: name 'boll' is not defined
>>> bool)( 3 )
SyntaxError: invalid syntax
>>> bool( 3 )
True
>>> bool( [] )
False
>>> 
>>> a = print( a < 0 )
False
>>> a= a < 0
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a= a < 0
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> a = a< 0
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a = a< 0
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> a= 1
>>> a = a < 0
>>> a
False
>>> bool( [ 1 ] )
True
>>> 
>>> 
>>> a = b'Python rules'
>>> a
b'Python rules'
>>> type( a )
<class 'bytes'>
>>> a > 0
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a > 0
TypeError: '>' not supported between instances of 'bytes' and 'int'
>>> 
>>> 
>>> 
>>> a = 23
>>> type( a )
<class 'int'>
>>> isinstance( a, int )
True
>>> b = 0o23
>>> c = 0x23
>>> d = 0b1101
>>> print( a, b, c, d )
23 19 35 13
>>> 2 ** 1024
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
>>> n = 2 **1024
>>> n.bit_length( )
1025
>>> 
>>> 

>>> a = 1.2
>>> type( a )
<class 'float'>
>>> isinstance( a, float )
True
>>> b =  3e3
>>> c = -0.2e-4
>>> print( a, b, c )
1.2 3000.0 -2e-05
>>> 
>>> 
>>> import sys; sys.float_info; sys.float_info.max; sys.float_info.min
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
1.7976931348623157e+308
2.2250738585072014e-308
>>> 
>>> 
>>> float( 'inf' )
inf
>>> float( '-inf' )
-inf
>>> infinity / 1000
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    infinity / 1000
NameError: name 'infinity' is not defined
>>> infinity = float( 'inf' )
>>> infinity / 1000
inf
>>> 
>>> 
>>> 
>>> a = 1.2
>>> a.is_integer( )
False
>>> a = 2.0
>>> a.is_integer( )
True
>>> 
>>> 
>>> round( 1.2 )
1
>>> round( 1.0 )
1
>>> import math
>>> math.ceil( 1.2 )
2
>>> math.floor( 1.9 )
1
>>> 
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> 5 % 2
1
>>> 5 % -3
-1
>>> -5 % 3
1
>>> divmod( 5, 2 )
(2, 1)
>>> 2 ** 3
8
>>> 2 **3 ** 2
512
>>> 5 ** -2.0
0.04
>>> 2 ** 9
512
>>> 
>>> 
>>> 6 == 9; 6 !=9, 1 > 3; 4 <=5
False
(True, False)
True
>>> 6 ==9; 6 !=9; 1 >3; 4 <=5
False
True
False
True
>>> a = 5; b = 10; a< b; 0 < a < b; 0 < a and a < b
True
True
True
>>>  a = 10; b = 30; a > 10 and b < 50
 
SyntaxError: unexpected indent
>>> a = 10
>>> b = 30
>>> a > 10 and b < 50
False
>>> True + 1
2
>>> False + 1
1
>>> a = 5
>>> b = 10
>>> s = a + b
>>> s
15
>>> a = 10
>>> b - 5
5
>>> s = a - b
>>> s
0
>>> a = 10
>>> b = 5
>>> s = a - b
>>> s
5
>>> a = 5
>>> b = 10
>>> s = a * b
>>> s
50
>>> a = 10
>>> b = 5
>>> s = a / b
>>> s
2.0
>>> s = a // b
>>> s
2
>>> s = a % b
>>> s
0
>>> 
>>> 
>>> no = 1
>>> subject1 = 50
>>> subject2 = 90
>>> subject3 = 80
>>> total = subject1 + subject2 + subject3
>>> avg = (suject1 + subject2 + subject3 ) / 3
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    avg = (suject1 + subject2 + subject3 ) / 3
NameError: name 'suject1' is not defined
>>> print( no, subject1, subject2, subject3, total )
1 50 90 80 220
>>> avg = ( subject1, subject2, subject3 ) / 3
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    avg = ( subject1, subject2, subject3 ) / 3
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
>>> avg = ( 50 + 90 + 80 ) / 3
>>> print( no, subject1, subject2, subject3, total, avg )
1 50 90 80 220 73.33333333333333
>>> avg = round((50 + 90 + 80 ) / 3, 2))
SyntaxError: invalid syntax
>>> avg = round((50 + 90 + 80 ) / 3, 2)
>>> avg
73.33
>>> print( no, subject1, subject2, subject3, total, avg )
1 50 90 80 220 73.33
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
1 50 90 80 220 73.33
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
1 50 90 80 220 73.33
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
1 50 90 80 220 73.33
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
15
1 50 90 80 220 73.33
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
15
5
50
2.0
2
0
1 50 90 80 220 73.33
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
int number: 5
int number2 : 10
1 50 90 80 220 73.33
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 14, in <module>
    i
NameError: name 'i' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
int number: 5
int number2 : 10
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 4, in <module>
    number + number2
NameError: name 'number' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
int number: 5
int number2 : 10
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 4, in <module>
    print(number + number2)
NameError: name 'number' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
int number: 5
int number2 : 10
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 4, in <module>
    print(number + number2)
NameError: name 'number' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15 [number =  5]
1 50 90 80 220 73.33
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 18, in <module>
    i
NameError: name 'i' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
1 50 90 80 220 73.33
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 18, in <module>
    i
NameError: name 'i' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 8, in <module>
    .format( number2, number1, (number2 - number) ))
NameError: name 'number1' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
>>> 
 5 + 10 = 15
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 8, in <module>
    .format( number2, number1, (number2 - number) ))
NameError: name 'number1' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 8, in <module>
    .format( number2, number1, (number2 - number) ))
NameError: name 'number1' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 8, in <module>
    .format( number2, number1, (number2 - number) ))
NameError: name 'number1' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 8 10 = 50
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 12, in <module>
    .format( number2, number, (number2 / number) ))
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 12, in <module>
    .format( number2, number, (number2 / number) ))
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 12, in <module>
    .format( number2, number, (number2 / number) ))
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 12, in <module>
    .format( number2, number, (number2 / number) ))
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 12, in <module>
    .format( number2, number, (number2 / number) ))
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 30, in <module>
    avg = round( toal / 3 , 2 )
NameError: name 'toal' is not defined
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 32, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
KeyError: '2;5'
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 32, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
KeyError: '2;5'
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 32, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============format( no, subject1, subject2, subject3, total, avg ) )
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 32, in <module>
    print( '\n{0:<5} {1:5} {2:5} {3:5} {4:5} {5:7} {6:8.2f}\n'.format( no, subject1, subject2, subject3, total, avg ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, avg ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, average ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, average ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, average ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0
Traceback (most recent call last):
  File "C:\Work Space\Python\Python 2일차 실습.py", line 33, in <module>
    format( no, subject1, subject2, subject3, total, average ) )
IndexError: tuple index out of range
>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0

1        50    90    80   220    73.33

>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0

1     50       90    80   220    73.33

>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0

1        50    90    80   220    73.33

>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
>>> 
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0

1        50    90    80   220    73.33

>>> 
=============== RESTART: C:\Work Space\Python\Python 2일차 실습.py ===============
 5 + 10 = 15
10 -  5 =  5
 5 * 10 = 50
10 /  5 = 2.000000
10 //  5 =  2
10 %  5 =  0

1        50    90    80   220    73.33

>>> 

'''
    training1_1.py

    Python 2일차 실습 #1

    1. 두 정수를 입력받아 다음과 같이 출력 되는 프로그램 작성

	    5 + 10 = 15
       10 -  5 = 10
        5 * 10 = 50
       10 /  5 =  2.00
       10 // 5 =  2
       10 %  5 =  0
'''
number1 = int( input( '첫 번째 정수를 입력하시요 : ' ) )
number2 = int( input( '두 번째 정수를 입력하시요 : ' ) )

result_add = number1 + number2
result_sub = number2 - number1
result_mul = number1 * number2
result_div = number2 / number1
result_div2 = number2 // number1
result_mod = number2 % number1

print( '{0:2} + {1:2} = {2:2}'.format( number1, number2, result_add ) )
print( '{0:2} - {1:2} = {2:2}'.format( number2, number1, result_sub ) )
print( '{0:2} * {1:2} = {2:2}'.format( number1, number2, result_mul ) )
print( '{0:2} / {1:2} = {2:.2f}'.format( number2, number1, result_div ) )
print( '{0:2} // {1:2} = {2:2}'.format( number2, number1, result_div2 ) )
print( '{0:2} % {1:2} = {2:2}'.format( number2, number1, result_mod ) )

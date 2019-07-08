'''
    training2_5.py

    Python 2일차 실습 #2

    5. 10개의 정수를 입력 받아 가장 큰 정수와 가장 작은 정수를 출력하는 프로그램
'''
import sys

max = sys.float_info.min
min = sys.float_info.max

for i in range( 1, 11, 1 ):
    number = int( input( '{0:3} 번째 정수 입력 : '.format( i ) ) )
    if number > max:
        max = number
    
    if number < min:
        min = number

print( '\nmaximum number : {0:8}'.format( max ) )
print( 'minimum number : {0:8}\n'.format( min ) )

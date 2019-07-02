'''
   inputprint.py

   이름, 나이 성별을 입력하여 출력하는 프로그램
'''

name = input( " 이름 입력 : " )
age = input( " 나이 입력 : " )
sex = input( " 성별 입력 : " )

print( name )
print( age )
print( sex )

number = 5
number2 = 10

print( ' %2d + %2d = %2d [ number = %2d ]'\
       % ( number, number2,( number + number2 ), number ) )

print( '{0:2d} + {1:2d} = {2:2d} [ number = {0:2d}]'\
       .format( number, number2, (number + number2 ) ))
       
print( '{0:2d} + '.format( number ), end = ' ' )
print( '{0:2d} = '.format( number2 ), end = ' \n ' )
print( '{0:2d}'.format( ( number + number2 ) ) )

'''
    training2_4.py

    Python 2일차 실습 #2

    4. 정수를 입력받아 해당하는 정수의 구구단표를 출력하며 정수가 
       0이면 종료하는 프로그램
'''
number = int( input( '구구단 출력을 원하는 정수를 입력 ( 0 : quit ) : ' ) )
while ( number != 0 ):
    print()
    for i in range( 1, 10 ):
        multiple = number * i
        print( '{0:5} X {1:5} = {2:8}'.format( number, i, multiple ) )
    print()
    number = int( input( '구구단 출력을 원하는 정수를 입력 ( 0 : quit ) : ' ) )


while ( True ):
    number = int( input( '구구단 출력을 원하는 정수를 입력 ( 0 : quit ) : ' ) )
    if number != 0:
        print()
        for i in range( 1, 10 ):
            multiple = number * i
            print( '{0:5} X {1:5} = {2:8}'.format( number, i, multiple ) )
        print()
    else:
        break


#print( )들은 없어도 됨

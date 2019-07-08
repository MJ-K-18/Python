'''
    training2_1.py

    Python 2일차 실습 #2

    1. 세 정수를 입력받아 큰 정수에서 작은 정수 순으로 출력하는 프로그램 작성
       첫번째 정수가 0이면 종료한다.
'''
number1 = int( input( '첫 번째 정수를 입력하시요 ( 0 : quit ) : ' ) )
while ( number1 != 0 ):
    number2 = int( input( '두 번째 정수를 입력하시요 : ' ) )
    number3 = int( input( '세 번째 정수를 입력하시요 : ' ) )

    if number1 > number2:
        if number1 > number3:
            maximum = number1
            if number2 > number3:
                midium = number2
                minimum = number3
            else:
                midium = number3
                minimum = number2
        else:
            maximum = number3
            midium = number1
            minimum = number2
    elif number2 > number3:
        maximum = number2
        if number1 > number3:
            midium = number1
            minimum = number3
        else:
            midium = number3
            minimum = number1    
    else:
        maximum = number3
        midium = number2
        minimum = number1

    print( '\nmax : {0:5}\tmid : {1:5}\tmin : {2:5}\n'.format( maximum, midium, minimum ) )
    
    number1 = int( input( '첫 번째 정수를 입력하시요 ( 0 : quit ) : ' ) )        

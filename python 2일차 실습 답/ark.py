while ( True ):
    number = int( input( '구구단 출력을 원하는 정수를 입력 ( 0 : quit ) : ' ) )
    if number != 0:

        for i in range( 1, 10 ):
            multiple = number * i
            print( '{0:5} X {1:5} = {2:8}'.format( number, i, multiple ) )

    else:
        break
        

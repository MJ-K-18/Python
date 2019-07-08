def calc_average( number1, number2 ):
    return ( number1 + number2 ) / 2

number1 = int( input( '첫 번째 정수 입력 ( -1 : quit ) : ' ) )
while ( number1 != -1 ):
    number2 = int( input( '두 번째 정수 입력 : ' ) )
    print( '\n{0:5} 과 {1:5}의 평균값은 : {2:7.2f}\n'.format( number1, number2, calc_average( number1, number2 ) ) )
    number1 = int( input( '첫 번째 정수 입력 ( -1 : quit ) : ' ) )

def max_min_select( data_list ):
    maximum = sys.float_info.min
    minimum = sys.float_info.max

    for value in data_list:
        if value > maximum:
            maximum = value
    
        if value < minimum:
            minimum = value

    return maximum, minimum


number_list = []

number = int( input( '\n정수 입력 ( -1 : 입력 종료 ) : ' ) )
while ( number != -1 ):
    number_list.append( number )
    number = int( input( '정수 입력 ( -1 : 입력 종료 ) : ' ) )

maximum, minimum = max_min_select( number_list )
print( '\n{0}의 최대값 {1:5}'.format( number_list, maximum ) )
print( '\n{0}의 최소값 {1:5}'.format( number_list, minimum ) )

input( '\nPress any key to program stop...' )
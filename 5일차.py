def allsum( a, b):
    return sum(range(min( a, b ), max( a, b ) + 1) )

number1 = int(input( ' 시작값 입력 : ' ) )
number2 = int(input( ' 끝값 입력 : ' ) )
if number1 < number2:
    fullsum = allsum( number1, number2 )
    print( '{0:2} 부터 {1:2}까지 모든 정수값의 합 : {2:2}'.format( number1, number2, fullsum))

def slice_str( a, b):
    return a.append( b[0:3] )

data_list = []
city = input( '도시 이름( end : quit ) : ')
while city != 'end':
    p3 = slice_str( data_list, city )

    city = input( '도시 이름( end : quit )  : ')


print( p3 )

data_list = []
city = input( '도시 이름( end : quit ) : ')
while city != 'end':
    data_list.append( city[0:3] )

    city = input( '도시 이름( end : quit )  : ')


print( data_list )
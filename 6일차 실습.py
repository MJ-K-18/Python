'''
1. 최고값을 구하는 함수 작성 : my_max( )
'''
def my_max( a ):

    MAX = a[ 0 ]

    for i in range( 1, len( a ) ):
        if a[ i ] > MAX:
            MAX = a[ i ]
    
    return MAX

print( my_max( (100,2,3,4,5) ) )

'''
2. 최저값을 구하는 함수 작성 : my_min( )
'''

def my_min( a ):

    MIN = a[ 0 ]

    for i in range( 1, len( a ) ):
        if a[ i ] < MIN:
            MIN = a[ i ]
    
    return MIN

print( my_min( [100,2,3,4,5] ) )


'''
3. 합계를 구하는 함수 작성 : my_sum( )
'''
def my_sum( a ):
    sum = 0
    for i in a:
        sum += i
    return sum

print( my_sum( (1,2,3,4,5,6) ))


'''
4. 평균을 구하는 함수 작성 : my_avg( )
'''
def my_avg( a ):

    avg = my_sum( a ) / len( a )

    return avg

print( my_avg( (1,2,3,4,5 ) ) )

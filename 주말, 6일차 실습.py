'''
1. my_join( ) 함수 구현 : str1과 str2 문자열을 결합해서 return하는 함수

  def my_join( str1, str2 ) :
'''


def my_join( a, b ):
    if a.isalpha() == True and b.isalpha() == True:
        result = a + ' ' + b
        
    elif a.isalpha() == False or b.isalpha() == False:
        result = '잘못된 입력입니다.'
    return result

print( my_join( 'hannam', 'university' ) )

print( my_join( '1123', 'hannam' ) )


def my_join1( a, b ):
    result = a + b
    return result

print( my_join1( 'asdfm' ,'234' ) )
print( my_join1( '12345', '6789') )


'''
2. my_split( ) 함수 구현 : str 내용중 ch를 기준으로 분리하여 list에 저장 후 
		        return하는 함수

  def my_split( str, ch ) :
'''


def my_split( a, b ):
    result = list(a.split( b ))
    return result

print( my_split( 'hannamuniversity', 'an' ))
print( my_split( '1234567', '45' ) )
print( my_split( '1,2,3,4,5,6,7', ',' ) )






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


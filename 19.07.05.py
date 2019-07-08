#함수 정의
def func1():               # 인수 없고, return 값도 없는 경우
    print( ' functional' )

def func2( a ):            # 인수 있고, return 값이 없는 경우
    print( a )

def func3():               # 인수 없고, return 값이 있는 경우
    return 5 + 10

def func4( a ):            # 인수 있고, return 값도 있는 경우
    total = 0
    for value in a:
        total += value
    return total

#함수 호출
func1( )
func2( 5 )
func2( (5, 10) )
func2( [ 1, 2, 3, 4, 5 ] )
func2( { 'one':1, 'two':1, 'three':3 } )

print( func3() )
print( func4( ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ) ) )




def gg( t ):
    #t = [ 1, 2, 3 ]
    t[1] = 60
    return

a = [ 5, 6 ,7 ]
gg( a )
print( a )

x = 10
y = 11
def foo( ):
    global x
    x = 20
    def bar( ):
        a = 30
        print( a, x, y )
    bar( )
    x = 40
    bar( )

foo( )
print( x, y )

print( len( 'apple' ) )

def my_len( data ):
    count = 0
    for i in range( len( data) ):
        count += 1

    return count

print( my_len( 'apple' ) )
print( my_len( [1, 2, 3, 4, 5 ] ) ) 

def my_compare( src, dest ):
    src_length = my_len( src )
    dest_length = my_len( dest )
    if src_length == dest_length:
        index = 0
        while ( index < src_length and src[ index ] == dest[ index ]):
            index += + 1
        if index == src_length:
            result = 'True'
        else:
            result = 'False'
    else:
        result = 'False'
    return result

print( my_compare( 'apple', 'orange' ) )
print( my_compare( 'apple', 'aPple' ) )






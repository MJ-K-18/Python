'''
    mylib.py
'''
# 함수 정의
def my_print( data ):
    length = len( data )
    for i in range( length ):
        print( '[{0:^5}] : {1}'.format( i, data[ i ] ) )

    return

# 함수 test
if __name__ == '__main__':
    l = [ 1, 2, 3 ]
    t = ( 10, 20, 30 )
    my_print( l )
    print( )
    my_print( t )

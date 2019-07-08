def my_join( a, b ):
    if a.isalpha() and b.isalpha():
        result = a + b
    else:
        result = '문자열이 아닙니다'
    return result

print( my_join( 'apple', 'orange' ) )



def my_split( a, b ):
    list = []
    list.append( a.split( b ) )

    return list

print( my_split( 'hannamuniversity', 'ni' ) )

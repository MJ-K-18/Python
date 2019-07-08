'''
    training5_4_weekend.py

    Python 5일차 주말 실습

    1. my_join() 함수 구현 : str1과 str2 문자열을 결합해서 return하는 함수
       def my_join( str1, str2 ):

    2. my_split() 함수 구현 : str 내용중 ch를 기준으로 분리하여 List에 저장 후
			  return 함수
       def my_split( str, ch ):
'''
# sequence 자료형 길이 계산
def my_len( data ):
    count = 0
    for ch in data:
        count += 1
    return count

# str1과 str2의 결합
def my_join( str1, str2 ):
    return str1 + str2

# str1에 ch를 결합
def my_join2( str1, ch ):
    str_len = my_len( str1 )
    ret_str = str1[ 0 ]
    ret_str += ch
    for i in range( 1, str_len ):
        ret_str += str1[ i ]
        if i != ( str_len - 1 ):
            ret_str += ch

    return ret_str

def my_split( str1, ch ):
    ret_str = []
    str_len = my_len( str1 )

    count = 0
    tmp_str = ''
    while count < str_len:
        if str1[ count ] != ch:
            tmp_str += str1[ count ]
        else:
            ret_str.append( tmp_str )
            tmp_str = ''
        count += 1
    ret_str.append( tmp_str )

    return ret_str

str1 = 'abcd'
str2 = 'efg'
str3 = my_join( str1, str2 )
print( 'my_join() -> str1 : {0}\tstr2 : {1}\tstr3 = {2}'.format( str1, str2, str3 ) )

str1 = 'abcd'
ch = ','
str3 = my_join2( str1, ch )
print( 'my_join2() -> str1 : {0}\tch : {1}\tstr3 = {2}'.format( str1, ch, str3 ) )

str1 = 'Life is too short'
ch = ' '
str3 = my_split( str1, ch )
print( 'my_split() -> str1 : {0}\tch : {1}\tstr3 = {2}'.format( str1, ch, str3 ) )

str1 = 'a:b:c:d'
ch = ':'
str3 = my_split( str1, ch )
print( 'my_split() -> str1 : {0}\tch : {1}\tstr3 = {2}'.format( str1, ch, str3 ) )

number = [ 10, 5, 12, 0 ,3.5, 99.5, 42 ]
func = [max(number), min(number), sum(number) ]
print( func )

# 문자는 ascii code 값을 기준으로 비교
str = 'helloWorld'
func = [ max(str), min(str) ]
print( func )

t = ( 10, 6, 9, 1, 3 )
func = [ max(t), min(t) ]
print( func )

s = ( 15, 11, 19, 3, -2 )
func = [ max(s), min(s) ]
print( func )

# dic은 key값을 기준으로 비교
d = { 'a' : 10, 'b' : 20, 'C' : 30 }
func = [ max(d), min(d) ]
print( func )


d = { 10 : 'a', 20 : 'b', 30 : 'C' }
func = [ max(d), min(d) ]
print( func )

# 절대값
print( [ abs( 10 ), abs( -10 ) ] )
print( [ abs( 2.45 ), abs( -2.45 ) ] )


# index와 value를 print
l = [ 'banana', 'apple', 'mango' ]
for i, v in enumerate( l ):
    print( '[{0}] : {1}'.format( i, v))

for i in range( len( l ) ):
    print( '[{0}] : {1}'.format( i, l[ i ]))
    
for v in l:
    print( '{0}'.format( v ))

# index를 key로 한 dic 생성
d = { i:j for i,j in enumerate( 'hello World apple banana mango victory'.split()) }
print( d )

# 같은 index 끼리 묶어주는 함수 zip
l1 = [ 'a1', 'a2', 'a3' ]
l2 = [ 'b1', 'b2', 'b3' ]
for a, b in zip( l1, l2 ):
    print( 'l1 : {0}\tl2 : {1}'.format( a, b ) )

a, b, c = zip( ( 1, 2, 3 ), ( 10, 20, 30 ), ( 100, 200, 300 ) )
print( '{0}\t{1}\t{2}'.format( a, b, c ) )

l = [ sum( x ) for x in zip( ( 1, 2, 3 ), ( 10, 20, 30 ), ( 100, 200, 300 ) ) ]
print( l )

for i, ( a, b ) in enumerate( zip( l1, l2 ) ):
    print( '[{0}] : {1} - {2}'.format( i, a, b ) )

# random 함수: 0.1 ~ 1.0까지의 임의의 수를 생성해줌[난수], 실행할때마다 다름
import random 
print( random.random() )
print( round( random.random() + 1 ) + 5 )

# randint 함수 : 정해진 값의 범위 내에서 임의의 수를 생성
data1 = random.randint( 1, 6 )
data2 = random.randint( 1, 6 )
print( '임의의 두 수 : {0} - {1}'.format( data1, data2 ) )

# randrange 함수 : 정해진 값의 범위 내에서 임의의 range 생성
data1 = random.randrange( 1, 10, 2 )
data2 = random.randrange( 0, 100, 10 )
print( '임의의 두 수 : {0} - {1}'.format( data1, data2 ) )

# choice 함수 : list 안에서 임의로 선택
menu = ['김치찌개', '된장찌개', '보쌈', '순두부찌개', '제육덮밥' ]
print( '오늘의 점심은 -> {0}'.format( random.choice( menu ) ) )

restaurant = ['코핫', '집밥', '밥풀', '마미하우스' ]
print( '어디로 가야하죠 아조씨 -> {0}'.format( random.choice( restaurant ) ) )


# sample 함수 : ( list, 임의의 수 ) / 임의의 수 만큼 list에서 선택 
print( random.sample( [ 1, 2, 3, 4, 5, ], 2 ) )


# 제어값의 사용처가 없는 경우 _ 를 사용할 수도 있음
for i in range( 10 ):
    print( "Hello, World!!" )

print( )
for _ in range( 10 ):
    print( "Hello, World!!" )


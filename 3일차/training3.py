'''
    training3.py

    Python 3일차 실습 #1
'''
question_str = '''
1. s = 'hong gil dong201412121623210' 을 다음과 같이 출력하는 프로그램
	
	Name : hong gil dong
	Birthday:2014/12/12
	ID Number : 20141212 - 1623210
'''
print( ''.center( 70, '=' ) )
print( question_str )
print( ''.center( 70, '=' ) )
print()

s = 'hong gil dong20141121623210'

name = s[ :s.rfind( 'g' ) + 1 ]
birthday_index = s.rfind( 'g' ) + 1
birthday = s[ birthday_index: birthday_index + 9 ]
idnumber = s[ s.rfind( 'g' ) + 1: ] 

print( 'Name : ' + name )
print( 'Birthday : ' + birthday[ :4 ] + '/' + birthday[ 4:6 ] + '/' + birthday[ 6:8 ] )
print( 'ID Number : ' + idnumber[ :8 ] + '-' + idnumber[ 8: ] )

input( '\nPress any key to continue...' )
print()

question_str = '''
2. s = 'Hannam University' 내용을 문자열 슬라이딩과 문자열 연결하기를 이용하여
   'University Hannam'로 변경하여 출력하는 프로그램
'''
print( ''.center( 78, '=' ) )
print( question_str )
print( ''.center( 78, '=' ) )
print()

s = 'Hannam University'

print( s[ s.find( 'University' ): ] + ' ' + s[ :s.find( 'University' ) ] )

input( '\nPress any key to continue...' )
print()

question_str = '''
3. s = 'hello world'의 내용을 'hi world'로 변경하여 출력하는 프로그램
'''
print( ''.center( 70, '=' ) )
print( question_str )
print( ''.center( 70, '=' ) )
print()

s = 'hello world'

print( 'hi' + ' ' + s[ s.find( 'world' ): ] )

input( '\nPress any key to continue...' )
print()

question_str = '''
4. 전화 번호를 '-'없이 번호만 입력 받아 다음과 같이 출력하는 프로그램
   전화 번호는 최소 10자, 최대 11자가 아니면 다시 입력 받는다.

	(010) 123-4567
	(010)1234-5678
'''
print( ''.center( 70, '=' ) )
print( question_str )
print( ''.center( 70, '=' ) )
print()

tel_number = input( "전화번호를 '-'없이 10~11자리 사이로 입력하세요 ( 0 : quit ): " )
while ( len( tel_number ) > 1 ):
    while ( not tel_number.isdigit() or 10 > len( tel_number ) or len( tel_number) > 11 ):
        print( '\nError : 잘못 입력하였습니다.\n숫자로만 10~11자리 사이로 입력하세요\n' )
        tel_number = input( "전화번호를 '-'없이 10~11자리 사이로 입력하세요 : " )

    if len( tel_number ) == 10:
        print( '\n({0:3}) {1:3}-{2:4}'.format( tel_number[ :3 ], tel_number[ 3:6 ], tel_number[ 6: ] ) )
    else: 
        print( '\n({0:3}){1:4}-{2:4}'.format( tel_number[ :3 ], tel_number[ 3:7 ], tel_number[ 7: ] ) )

    tel_number = input( "\n전화번호를 '-'없이 10~11자리 사이로 입력하세요 ( 0 : quit ): " )

input( '\nPress any key to program stop...' )

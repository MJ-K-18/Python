<<<<<<< HEAD
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
=======
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

#4
def input_student_info( ):
    MAX = 10
    SUBJECT = 3
    count = 0

    name = input( '학생 이름 입력 ( "end" : quit ) : ' )
    while name != 'end' and count < MAX:
        count = count + 1
        subjects = []
        for x in range( SUBJECT ):
            subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )
            while ( subject < 0 or subject > 100 ):
                print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )

        name = input( '학생 이름 입력 ( "end" : quit ) : ' )
    return students[ name ] = student

input_student_info(  )

clac_score_table( )



>>>>>>> bb151931495707a0cbffd450015c799fa0aa3ed5

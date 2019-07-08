'''
    training5_3.py

    Python 5일차 실습 #1
'''
def input_student_info( students ):
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
            subjects.append( subject )
        
        student = []
        student.append( name )
        student.append( subjects )

        students[ name ] = student

        name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

    return

def calc_score_table( students ):
    student_list = list( students.keys() )

   
    for name in student_list:
        total = 0
        for subject in students[ name ][ 1 ]:
            total += subject

        average = total / SUBJECT
        if average >= 90:
            grade = 'Excellent'
        elif average <= 60:
            grade = 'Fail'
        else:
            grade = ' '

        students[ name ].append( total )
        students[ name ].append( average )
        students[ name ].append( grade )
    
    return
    
def calc_rank( students ):
    keys = list( students.keys() )

    for i in range( len( students ) ):
        students[ keys[ i ] ].append( 1 )
        for j in range( len( students ) ):
            if students[ keys[ i ] ][ 3 ] < students[ keys[ j ] ][ 3 ]:
                students[ keys[ i ] ][ 5 ] += 1

    return

def print_score_table( students ):
    keys = list( students.keys() )

    print()
    for student_name in keys:
        print( '{0:<10}'.format( students[ student_name ][ 0 ] ), end = '' )
        for subject in students[ student_name ][ 1 ]:
            print( '{0:3}'.format( subject ), end = '' )
        print( '{0:5} {1:6.2f} {3:2} {2:<10}'.format( students[ student_name ][ 2 ], 
                                                    students[ student_name ][ 3 ], 
                                                    students[ student_name ][ 4 ],  
                                                    students[ student_name ][ 5 ] ) )

    return

question_str = '''
5. 다음과 같이 출력하는 프로그램( dictionary 이용, 함수작성 )
   ( 10명이내 이름이 'end'이면 결과 출력, 90이상 Excellent 60이하 Fail )

    Hong 50 50 50 150 50.0 3 Fail
    Kim  90 90 90 270 90.0 1 Excellent
    Nam  70 70 70 210 70.0 2
'''
print( ''.center( 72, '=' ) )
print( question_str )
print( ''.center( 72, '=' ) )
print()

MAX = 10
SUBJECT = 3

students = {}

input_student_info( students )
calc_score_table( students )
calc_rank( students )
print_score_table( students )

input( '\nPress any key to program stop...' )

import Student1

def main():
    MAX = 10
    SUBJECT = 3

    students = []
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
        student = Student1.Student( name, subjects[0], subjects[1], subjects[2] )
        students.append( student )
       
        name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

    print()
    for i in students:
        student = i.readStudentInfo()

        print( '{0:<10}'.format( student[ 0 ] ), end = '' )
        print( '{0:3} {1:3} {2:3}'.format( student[ 1 ], student[ 2 ], student[ 3 ] ), end = '' )
        print( '{0:5} {1:6.2f} {2:<10}'.format( student[ 4 ], student[ 5 ], student[ 6 ] ) )

if __name__ == '__main__':
    main()
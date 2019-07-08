# 1
MAX = 10
SUBJECT = 3

students = {}
count = 0

name = input( '학생 이름 입력 ( "end" : quit ) : ' )
while name != 'end' and count < MAX:
    count = count + 1
    subjects = []
    total = 0
    for x in range( SUBJECT ):
        subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )
        while ( subject < 0 or subject > 100 ):
            print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
            subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( SUBJECT, x + 1 ) ) )

        subjects.append( subject )
        total += subject

    average = total / SUBJECT
    rank = 1



    if average >= 90:
        grade = 'Excellent'
    elif average <= 60:
        grade = 'Fail'
    else:
        grade = ' '

    student = []
    student.append( name )
    student.append( subjects )
    student.append( total )
    student.append( average )
    student.append( rank )
    student.append( grade )

    students.append( student )
    
    name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

for i in range( len( students ) ):
    for j in range( len ( students ) ):
         if students[ i ][ 2 ] < students[ j ][ 2 ]:
             students[ i ][ 4 ] += 1
print()
for student in students:
    print( '{0:<10}'.format( student[ 0 ] ), end = '' )
    for subject in student[ 1 ]:
        print( '{0:3}'.format( subject ), end = '' )
    print( '{0:5} {1:6.2f} {2:3} {3:<10}'.format( student[ 2 ], student[ 3 ], student[ 4 ], student[ 5 ] ) )

input( '\nPress any key to program stop...' )


#2




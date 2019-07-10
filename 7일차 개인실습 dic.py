def inputdata():
    students = {}
    count = 0
    MAX = 10
    name = str(input( '학생이름 입력( "end" : quit ) : '))
    while name != 'end' and count < MAX:
        count = count + 1
        student = []
        for i in range( 1, 2 ):
            score = int(input( '점수 입력 : ' ))
        student.append( name )
        student.append( score )

        students[ name ] =  student 
        name = str(input( '학생이름 입력( "end" : quit )  : '))
    return students

def avg_s( students ):
    keys = list(students.keys())
    allscore = []
    total = 0
    for name in keys:
        allscore.append(students[ name ][1] )
    for i in range(len(allscore)):
        total += allscore[i]
        avg = total / len( allscore )
    return avg

def max_s( students ):
    import sys
    max = sys.float_info.min

    s_score = []
    keys = list(students.keys())

    for name in keys:
        s_score.append(students[ name ][1] )

    for i in range(len(s_score)):
        if max < s_score[ i ]:
            max = s_score[ i ]
    high = max
    for name in keys:
        if students[ name ][ 1 ] == high:
            high_s = students[ name ]
    return high_s

def min_s( students ):
    import sys
    min = sys.float_info.max

    s_score = []
    keys = list(students.keys())

    for name in keys:
        s_score.append(students[ name ][1] )

    for i in range(len(s_score)):
        if min > s_score[ i ]:
            min = s_score[ i ]
    low = min
    for name in keys:
        if students[ name ][ 1 ] == low:
            low_s = students[ name ]
    return low_s

def s_count( students ):

    s_score = []
    keys = list(students.keys())
    score_count10 = []
    score_count20 = []
    score_count30 = []
    score_count40 = []
    score_count50 = []
    score_count60 = []
    score_count70 = []
    score_count80 = []
    score_count90 = []
    s_count = []
    for name in keys:
        s_score.append(students[ name ][1] )
    
    for name in keys:
        if 10 <= students[ name ][1] <20:
            score_count10.append( students[ name ][1] )
        if 20 <= students[ name][1] < 30:
            score_count20.append( students[ name ][1] )       
        if 30 <= students[ name][1] < 40:
            score_count30.append( students[ name ][1] )
        if 40 <= students[ name][1] < 50:
            score_count40.append( students[ name ][1] )
        if 50 <= students[ name][1] < 60:
            score_count50.append( students[ name ][1] )
        if 60 <= students[ name][1] < 70:
            score_count60.append( students[ name ][1] )
        if 70 <= students[ name][1] < 80:
            score_count70.append( students[ name ][1] )
        if 80 <= students[ name][1] < 90:
            score_count80.append( students[ name ][1] )    
        if 90 <= students[ name][1] < 100:
            score_count90.append( students[ name ][1] )
    s_count.append( score_count10 )
    s_count.append( score_count20 )
    s_count.append( score_count30 )
    s_count.append( score_count40 )
    s_count.append( score_count50 )
    s_count.append( score_count60 )
    s_count.append( score_count70 )
    s_count.append( score_count80 )
    s_count.append( score_count90 )

    return s_count
def printdata( students ):
    student = students
    max_score_student = max_s( students )
    min_score_student = min_s( students )
    average = avg_s( students )
    clacount = s_count( students )

    print( )
    for student in students:
            print( '{0:<10}'.format( student[ 0 ] ), end = '' )
            print( '{0:5}'.format( student[ 1 ] ) )
    print( '최고점수 학생 {0:5} 의 점수 : {1:2}'.format(max_score_student[0], max_score_student[1]) )
    print( '최저점수 학생 {0:5} 의 점수 : {1:2}'.format(min_score_student[0], min_score_student[1]) )
    print( '전체 평균값 : {0:2}'.format(average) )
    print( '10점대학생수 : {0:2} '.format( len(clacount[0]) ))
    print( '20점대학생수 : {0:2} '.format( len(clacount[1]) ))
    print( '30점대학생수 : {0:2} '.format( len(clacount[2]) ))
    print( '40점대학생수 : {0:2} '.format( len(clacount[3]) ))
    print( '50점대학생수 : {0:2} '.format( len(clacount[4]) ))
    print( '60점대학생수 : {0:2} '.format( len(clacount[5]) ))
    print( '70점대학생수 : {0:2} '.format( len(clacount[6]) ))
    print( '80점대학생수 : {0:2} '.format( len(clacount[7]) ))
    print( '90점대학생수 : {0:2} '.format( len(clacount[8]) ))
    return

students = inputdata( )


printdata( students )




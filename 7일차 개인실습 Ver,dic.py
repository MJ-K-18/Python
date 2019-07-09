def inputdata():
    students = {}
    count = 0
    MAX = 10
    name = str(input( '학생이름 입력 : '))
    while name != 'end' and count < MAX:
        count = count + 1
        student = []
        for i in range( 1, 2 ):
            score = int(input( '점수 입력 : ' ))
        student.append( name )
        student.append( score )

        students[ name ] =  student 
        name = str(input( '학생이름 입력 : '))
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

students = inputdata( )

print(avg_s( students ))
print(max_s( students ))
print(min_s( students ))


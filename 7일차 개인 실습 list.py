'''
1. 10명의 학생 이름, 점수를 입력 받아, 10명의 학생 이름, 점수를 출력하고
   최고점 학생 정보, 최저점 학생 정보, 평균 점수, 점수대 인원수를 출력하는
   프로그램( 함수로 구현 )
'''


def inputdata( ):

    for j in range( 10 ):
        name = str(input( '학생이름입력 : ' ))
        score = int( input(' 학생성적 입력 : ') )
        student =[ name, score ]
        students.append( student )

    return students

def printdata( students ):
    student = students
    max_score_student = max_score( students )
    min_score_student = min_score( students )
    average = calc_average( students )
    score_count10 = score_count( students, 10 )
    score_count20 = score_count( students, 20 )
    score_count30 = score_count( students, 30 )
    score_count40 = score_count( students, 40 )
    score_count50 = score_count( students, 50 )
    score_count60 = score_count( students, 60 )
    score_count70 = score_count( students, 70 )
    score_count80 = score_count( students, 80 )
    score_count90 = score_count( students, 90 )

  
    print( )
    for student in students:
            print( '{0:<10}'.format( student[ 0 ] ), end = '' )
            print( '{0:5}'.format( student[ 1 ] ) )
    print( '최고점수 학생 {0:5} 의 점수 : {1:2}'.format(max_score_student[0], max_score_student[1]) )
    print( '최저점수 학생 {0:5} 의 점수 : {1:2}'.format(min_score_student[0], min_score_student[1]) )
    print( '전체 평균값 : {0:2}'.format(average) )
    print( '10점대 인원수 : {0:2}'.format( score_count10))
    print( '20점대 인원수 : {0:2}'.format( score_count20))
    print( '30점대 인원수 : {0:2}'.format( score_count30))
    print( '40점대 인원수 : {0:2}'.format( score_count40))
    print( '50점대 인원수 : {0:2}'.format( score_count50))
    print( '60점대 인원수 : {0:2}'.format( score_count60))
    print( '70점대 인원수 : {0:2}'.format( score_count70))
    print( '80점대 인원수 : {0:2}'.format( score_count80))
    print( '90점대 인원수 : {0:2}'.format( score_count90))
    return


def calc_average( students ):
    
    total = 0
    for i in range(len(students)):
        total += students[i][1]
    average = total / 10
    return average


def max_score( students ):

    max = sys.float_info.min

    for i in range( 10 ):
        if max < students[ i ][1]:
            max = students[ i ][1]
        high = max
    highest = []
    for i in range( 10 ):
        if high == students[ i ][1]:
            highest.append( students[i][0] )
            highest.append( students[i][1] )
    return highest

def min_score( students ):

    min = sys.float_info.max

    for i in range( 10 ):
        if min > students[ i ][1]:
            min = students[ i ][1]
        low = min
    lowest = []
    for i in range( 10 ):
        if low == students[ i ][1]:
            lowest.append( students[i][0] )
            lowest.append( students[i][1] )
    return lowest

def score_count( students, avg ):
    score_counts = []
    for i in range(10):
        if (students[i][1]//10 == avg//10):
            score_counts.append(students[i][0])

    return len(score_counts)

import sys

MAX = 10

students = []

students = inputdata( )

printdata( students )

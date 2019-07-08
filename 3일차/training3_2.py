'''
    training3.py

    Python 3일차 실습 #2
'''
question_str = '''
1. 10개의 정수를 리스트에 저장한 후 가장 큰값과 가장 작은 값을 출력하는 프로그램
'''
print( ''.center( 80, '=' ) )
print( question_str )
print( ''.center( 80, '=' ) )
print()

numbers = []

for i in range( 1, 11 ):
    number = int( input( '{0:2}중 {1:2}번째 정수 입력 : '.format( 10, i ) ) )
    numbers.append( number )

max = numbers[ 0 ]
min = numbers[ 0 ]

for value in numbers:
    if value > max:
        max = value

    if value < min:
        min = value

print( '\nmaximum number : {0:8}'.format( max ) )
print( 'minimum number : {0:8}\n'.format( min ) )

input( '\nPress any key to continue...' )
print()

question_str = '''
2. 구구단표를 리스트 이용하여 출력하는 프로그램
'''
print( ''.center( 47, '=' ) )
print( question_str )
print( ''.center( 47, '=' ) )
print()

# List Indexing을 이용한 방법
multiples = [ [], [], [], [], [], [], [], [], [] ]

for i in range( 8 ):
    for j in range( 9 ):
        multiples[ i ].append( ( i + 2 ) * ( j + 1 ) )

print( '* List Indexing을 이용한 방법' )
for i in range( 8 ):
    for j in range( 9 ):
        print( '{0:3}'.format( multiples[ i ][ j ] ), end = '' )
    print()
print()

# List Comprehension를 이용한 방법
multiples = [ x * y for x in range( 2, 10 ) for y in range( 1, 10 ) ]
count = 0

print( '* List Comprehension를 이용한 방법' )
for x in range( 8 * 9 ):
    count = count + 1
    print( '{:3}'.format( multiples[ x ] ), end = '' )
    if count % 9 == 0:
        print()
        count = 0
print()

# List Comprehension를 이용한 방법 2
multiples = [ x * y for x in range( 2, 10 ) for y in range( 1, 10 ) ]
start = 0

print( '* List Comprehension를 이용한 방법 2' )
for x in range( 9, 81, 9 ):
    print( '{0[0]:3}{0[1]:3}{0[2]:3}{0[3]:3}{0[4]:3}{0[5]:3}{0[6]:3}{0[7]:3}{0[8]:3}'\
           .format( multiples[ start:x ] ) )
    start = start + 9

input( '\nPress any key to continue...' )
print()

question_str = '''
3. 리스트를 이용하여 아래와 같이 출력하는 프로그램
   1 2 3 4
   2 3 4 1
   3 4 1 2
   4 1 2 3
'''
print( ''.center( 50, '=' ) )
print( question_str )
print( ''.center( 50, '=' ) )
print()

l = list( range( 1, 5 ) )
list_length = len( l )

for value in l:
    print( '{0:3}'.format( value ), end = '' )
print()

for i in range( list_length - 1 ):
    temp = l[ 0 ]
    for j in range( list_length - 1 ):
        l[ j ] = l[ j + 1 ]
    l[ list_length - 1 ] = temp
    for value in l:
        print( '{0:3}'.format( value ), end = '' )
    print()
print()

question_str = '''
4. 다음과 같이 출력하는 프로그램
   ( 10명이내 이름이 'end'이면 결과 출력, 90이상 Excellent 60이하 Fail )

    Hong 50 50 50 150 50.0 Fail
    Kim  90 90 90 270 90.0 Excellent
    Nam  70 70 70 210 70.0
'''
print( ''.center( 80, '=' ) )
print( question_str )
print( ''.center( 80, '=' ) )
print()

MAX = 10
SUBJECT = 3

students = []
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
    student.append( grade )

    students.append( student )
    
    name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

print()
for student in students:
    print( '{0:<10}'.format( student[ 0 ] ), end = '' )
    for subject in student[ 1 ]:
        print( '{0:3}'.format( subject ), end = '' )
    print( '{0:5} {1:6.2f} {2:<10}'.format( student[ 2 ], student[ 3 ], student[ 4 ] ) )

input( '\nPress any key to program stop...' )

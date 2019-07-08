'''
    training1_2.py

    Python 2일차 실습 #1

    2. 번호, 과목1점수, 과목2점수, 과목3점수를 입력받아 다음과 같이
       출력 되는 프로그램

	1	50	90	80	220	73.33
'''
no = int( input( '번호를 입력하시요 : ' ) )
subject1 = int( input( '과목1 점수를 입력하시요 : ' ) )
subject2 = int( input( '과목2 점수를 입력하시요 : ' ) )
subject3 = int( input( '과목3 점수를 입력하시요 : ' ) )

total = subject1 + subject2 + subject3
average = total / 3


print( '\n{0:<5} {1:5} {2:5} {3:5} {4:5} {5:7} {6:8.2f}\n'.\
        format( no, subject1, subject2, subject2, subject3, total, average ) )

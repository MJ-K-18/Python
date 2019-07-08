'''
    training2_3.py

    Python 2일차 실습 #2

    3. 1 ~ 1000사이의 3의 배수와 5의 배수를 출력하는데 한 줄에 10개씩 출력하며,
       마지막에 3의 배수와 5의 배수의 합을 출력 하는 프로그램
'''
three_five_multiple_sum = 0
line_count = 0

for i in range( 1, 1001, 1 ):
    three_multiple = i % 3
    five_multiple = i % 5

    if three_multiple == 0 or five_multiple == 0:
        three_five_multiple_sum += i
        print( '{0:5}'.format( i ), end = '' )
        line_count += 1
    
        if line_count == 10:
            line_count = 0
            print()

print( '\n\n1 ~ 1000사이의 3의 배수와 5의 배수의 합 : {0:8}'.format( three_five_multiple_sum ) )

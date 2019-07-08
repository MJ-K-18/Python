'''
    training2_2.py

    Python 2일차 실습 #2

    2. 10개의 정수를 입력받아 양수 개수, 음수 개수, 양수일 때 짝수 개수, 홀수 개수
       출력 되는 프로그램
'''
positive = 0
negative = 0
even = 0
odd = 0
error = 0

for i in range( 1, 11, 1 ):
    number = int( input( '{0:3} 번째 정수 입력 : '.format( i ) ) )
    if number != 0:
        if number > 0:
            positive += 1
            remain = number % 2
            
            if remain == 0:
                even += 1
            else:
                odd += 1
        else:
            negative += 1
    else:
        error += 1

print( '\npositive count : {0:3}'.format( positive ) )
print( '\teven count : {0:3}\n\todd count :  {1:3}'.format( even, odd ) )
print( 'negative count : {0:3}'.format( negative ) )    
print( '\nerror count : {0:3}\n'.format( error ) )

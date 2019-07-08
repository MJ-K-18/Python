'''
    training6_1.py

    Python 6일차 실습 #1

    1. 최고값을 구하는 함수 작성 : my_max()
    2. 최저값을 구하는 함수 작성 : my_min()
    3. 합계를 구하는 함수 작성 : my_sum()
    4. 평균을 구하는 함수 작성 : my_avg()
'''
import sys

# sequence 자료형 길이 계산
def my_len( data ):
    count = 0
    for ch in data:
        count += 1
    return count

def my_max( datas ):
    ret_max = sys.float_info.min

    for value in datas:
        if ret_max < value:
            ret_max = value

    return ret_max

def my_min( datas ):
    ret_min = sys.float_info.max

    for value in datas:
        if ret_min > value:
            ret_min = value

    return ret_min

def my_sum( datas ):
    ret_sum = 0
    length = my_len( datas )

    for i in range( length ):
        ret_sum += datas[ i ]

    return ret_sum

def my_avg( datas ):
    ret_avg = 0.0
    length = my_len( datas )

    total = my_sum( datas )
    ret_avg = total / length

    return ret_avg

datas = [ 5, 7, 2, 4, 8, 1, 3, 6, 10, 9 ]

print( 'datas -> {0}\n'.format( datas ) )
print( 'datas max number -> {0}'.format( my_max( datas ) ) )
print( 'datas min number -> {0}'.format( my_min( datas ) ) )
print( 'datas sum number -> {0}'.format( my_sum( datas ) ) )
print( 'datas average number -> {0:.2f}'.format( my_avg( datas ) ) )

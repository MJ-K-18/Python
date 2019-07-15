f = open( 'sample.txt', 'w' )
for i in range( 1, 10 ):
    s = '{0:2} X {1:2} = {2:2}\n'.format( 3, i, 3 * i )
    f.write( s )
f.close()

print('\tsample.txt 내용 Lodad' )
f = open( 'sample.txt', 'r' )
data = f.read()    # 파일전체 읽기
print( data )
f.close()

print( '\tsample.txt 내용 2차 Load' )
f = open( 'sample.txt', 'r' )
line = f.readline() # 한줄씩 읽기
while line:
    print( line, end = '' )
    line = f.readline()
f.close()

print( '\tsample.txt 내용 3차 Load' )
f = open( 'sample.txt', 'r' )
lines = f.readlines() # 파일 내용을 읽어서 리스트로 변환
for line in lines:
    print( line )
f.close()

print( '\tsample.txt 내용 4차 Load' )
f = open( 'sample.txt', 'r' )
for line in f:
    print( line, end = '' )
f.close()

print( '\tsample.txt 내용 5차 Load' )
with open( 'sample.txt', 'r' ) as f: # with문을 쓰면 close를 따로 안해도 된다
    lines = f.readlines() 
    for line in lines:
        print( line )

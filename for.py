for i in range( 1, 10, 1 ):
    print( i )

for i in range( 1, 10, 2 ):
    print( i )

sum = 0
for number in range( 1, 11, 1 ):
    sum = sum + number
print( sum )


for i in range( 1, 11, 1):
    if i > 4:
        break
    print( i )






for i in range( 10 ):
    break
    print( i, end = ' ' )
else:
    print( 'else' )

print( 'end' )

#break가 있으면 else 부분이 작동하지 않음

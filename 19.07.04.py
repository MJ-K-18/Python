#comprehension

result = []
for i in range( 10 ):
    result.append( i )
print( result )

result = [ i for i in range( 10 ) ]
print( result )

#구구단
result = [ i * j for i in range( 2, 10 ) for j in range( 1, 10 ) ]
print( result )

#3의 배수만 result에 표시
result = []
for i in range( 1, 101 ):
    if ( i % 3 ) == 0:
        result.append( i )
print( result )

result = [ i for i in range( 1, 101 ) if ( i % 3) == 0]
print( result )


words = "The quick brown fox jumps over the lazy dog".split()
print(words)
result = [ [w.upper(), w.lower(), len(w) ] for w in words ]
print( result )



#순위 계산 algorithm
l = [ [ 5, 1 ], [ 3, 1 ], [ 1, 1 ], [ 4, 1 ], [ 2, 1 ] ]
for i in range( len( l ) ):
    for j in range( len ( l ) ):
        if l[ i ][ 0 ] < l[ j ][ 0 ]:
            l[ i ][ 1 ] += 1
for value in l:
    print( '{0:3} {1:3}'.format( value[ 0 ], value[ 1 ] ) )


#selection sort, 오름차순
for i in range( len( l ) - 1 ):
    k = i
    for j in range( i + 1, len ( l ) ):
        if l[ k ][ 0 ] < l[ j ][ 0 ]:
            k = j
        if k != i:
          temp = l[ k ]
          l[ k ] = l[ i ]

          l[ i ] = temp

for value in l:
   print( '\n{0:3} {1:3}'.format( value[ 0 ], value[ 1 ] ) )

#selection sort, 내림차순
for i in range( len( l ) - 1 ):
    k = i
    for j in range( i + 1, len ( l ) ):
        if l[ k ][ 0 ] > l[ j ][ 0 ]:
            k = j
        if k != i:
          temp = l[ k ]
          l[ k ] = l[ i ]
          l[ i ] = temp

for value in l:
   print( '\n{0:3} {1:3}'.format( value[ 0 ], value[ 1 ] ) )





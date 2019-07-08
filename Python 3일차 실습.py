s = 'hong gil dong 201412121623210'

name = s[ :s.rfind('g')+1]
birthday_index = s.rfind('g')+1
birthday = s[birthday_index : birthday_index + 9 ]
idnumber = s[ s.rfind('g') +1 : ]

print( 'Name : ' + name )
print( 'Bithday : ' + birthday[ :5] + '/' + birthday[5:7] + '/' + birthday[7:9] )
print( 'ID Number : ' + idnumber[ : 9 ] + '-' + idnumber[ 9: ] )


s = 'Hannam University'

print( s[ s.find('University'):] +' '+ s[ :s.find('University')])
    
s = 'hello world'

print( 'hi'+ ' ' + s[ s.find('world') : ] )


number = input( '전화번호' )
while ( len( number ) > 1 ):
    while ( not number.isdigit() or 10 > len( number) or len( number) > 11 ):
        print( 'Error' )
        number = input( '전화번호' )

    if len(number ) == 10:
        print( '({0:3}) {1:3}-{2:4}'.format( number[ :3 ], number[ 3:6 ], number[ 6: ] ) )
    else:
        print( '({0:3}){1:4}-{2:4}'.format( number[ :3 ], number[ 3:7 ], number[ 7: ] ) )
        number = input( '전화번호' )
    
    number = input( '전화번호')

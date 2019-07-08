<<<<<<< HEAD

name = input( '이름 : ')
while ( name != 'end' ):
     subject1 = int(input('1과목'))
     subject2 = int(input('2과목'))
     subject3 = int(input('3과목'))
     total = subject1 + subject2 + subject3
     average = total / 3     
     if average >= 90:
         status = input( 'Excellent' )
     elif average <= 60:
          status = input( 'Fail' )
     else:
         status = input('')
           
     print( '\n{0:<5} {1:5} {2:5} {3:5} {4:5} {5:7} {6:8.2f} {7:15}\n'.format( name, subject1, subject2, subject2, subject3, total, average, status ))
     
     name = input('이름: ')
=======

name = input( '이름 : ')
while ( name != 'end' ):
     subject1 = int(input('1과목'))
     subject2 = int(input('2과목'))
     subject3 = int(input('3과목'))
     total = subject1 + subject2 + subject3
     average = total / 3     
     if average >= 90:
         status = input( 'Excellent' )
     elif average <= 60:
          status = input( 'Fail' )
     else:
         status = input('')
           
     print( '\n{0:<5} {1:5} {2:5} {3:5} {4:5} {5:7} {6:8.2f} {7:15}\n'.format( name, subject1, subject2, subject2, subject3, total, average, status ))
     
     name = input('이름: ')
>>>>>>> bb151931495707a0cbffd450015c799fa0aa3ed5

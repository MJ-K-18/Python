number = int( 5 )
number2 = int( 10 )


print( '{0:2d} + {1:2d} = {2:2d}'\
       .format( number, number2, (number + number2) ))
print( '{0:2d} - {1:2d} = {2:2d}'\
       .format( number2, number, (number2 - number) ))
print( '{0:2d} * {1:2d} = {2:2d}'\
       .format( number, number2, (number * number2) ))
print( '{0:2d} / {1:2d} = {2:2f}'\
       .format( number2, number, (number2 / number) ))
print( '{0:2d} // {1:2d} = {2:2d}'\
       .format( number2, number, (number2 // number) ))
print( '{0:2d} % {1:2d} = {2:2d}'\
       .format( number2, number, (number2 % number) ))









no = 1
subject1 = int( 50 )
subject2 = int( 90 )
subject3 = int( 80 )
total = int( subject1 + subject2 + subject3 )
average = total / 3 
print( '\n{0:<5} {1:5} {2:5} {3:5} {4:5} {5:8.2f}\n'.\
       format( no, subject1, subject2, subject3, total, average ) )

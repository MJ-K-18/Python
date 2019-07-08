<<<<<<< HEAD
l = [ -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

import sys

max = sys.float_info.min
min = sys.float_info.max

for i in l :
    if i > max:
        max = i
        
    if i < min:
        min = i

print( '\nmaximum number : {0:8}'.format( max ) )
print( 'minimum number : {0:8}\n'.format( min ) )


=======
l = [ -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

import sys

max = sys.float_info.min
min = sys.float_info.max

for i in l :
    if i > max:
        max = i
        
    if i < min:
        min = i

print( '\nmaximum number : {0:8}'.format( max ) )
print( 'minimum number : {0:8}\n'.format( min ) )


>>>>>>> bb151931495707a0cbffd450015c799fa0aa3ed5

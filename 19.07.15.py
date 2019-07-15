# IDLE 에서 각각 쳐서 확인해 볼 것

a, b = 5, 0
c = a / b # error

4 + 'spam' + 3 #error

'3' + 3 #error

try:
    '3' + 3
except TypeError:
    print( 'Exception : Type error ... stop program' )

try:
    '3' + 3
except Exception:
    print( ' Exception : stop program' )

try:
	'3' + 3
except Exception as e:
	print( ' Exception [{0}] : stop program'.format( e ) )

try:
	3 + 3
except Exception as e :
	print( ' Exception [{0}] : stop program'.format( e ) )
else:
	print( 'stop program' )

try:
	'3' + 3
except Exception as e:
	print( ' Exception [{0}] : stop program'.format( e ) )
finally:
	print( 'Have a nice day^^' )


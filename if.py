a = 10
if a > 5:
	print('Big')
else:
	print('Small')

if a > 5: print( 'Big' )
else: print( 'Small' )


n = -2
if n > 0:
	print( 'Positive' )
elif n < 0:
	print( 'Negative' )
else:
	print( 'Zero' )


order = 'spagetti'
if order == 'spam':
	price = 500
elif order == 'ham':
	price = 700
elif order == 'egg':
	price = 300
elif order == 'spagetti':
	price = 900
else:
	price = 0
	
print( price )


a = 100
if a > 0:
	if a > 100:
		print( 'a > 100' )
	else:
		print( 'a < 100' )
else:
	if a < -100:
		print( 'a < -100' )
	else:
		print( 'a > -100' )

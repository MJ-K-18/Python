def inc( a, step = 1 ):
    return a + step

b = 1
b = inc( b )
print( b )
b = inc( b, 10 )
print( b )


#error
'''
def inc1( step = 1, a ):
    return a + step
 
b = 1
b = inc1( b )
print( b )
b = inc1( b, 10 )
print( b )
'''

def inc2( a = 1, step = 1 ):
    return a + step

b = 1
b = inc2( b )
print( b )
b = inc2( b, 10 )
print( b )
print( inc2 ( ) )


def area( height, width ):
    return height * width

area( 10, 20 )
area( width = 20, height = 10 )
# error
# area( width = 10, 20 )
area( 20, width = 10 )

def varg( a, *arg ):
    print( a, arg )

varg( 1 )
varg( 2, 3 )
varg( 2, 3, 4, 5, 6 )


def varg( *arg ):
    print( arg )

varg( 1 )
varg( 2, 3 )
varg( 2, 3, 4, 5, 6 )

#error
'''
def varg( *arg, *arg2 ):
    print( arg, arg2 )

varg( 1 )
varg( 2, 3 )
varg( 2, 3, 4, 5, 6 )
'''

def varg( a, b = 1,*arg ):
    print( a, b, arg )

varg( 1 )
varg( 2, 3 )
varg( 2, 3, 4, 5, 6 )

def f( width, height,**kw ):
    print( width, height )
    print( kw )

f( width = 10, height = 5, depth = 10, dimension =3 )


def f2( *args, **kw ):
    print( args )
    print( kw )

f2( 1, 2, width = 10, height = 20 )
f2( 3, 4, 5, 6, width = 10, height = 20, depth = 30, diension = 5 )
f2( 10 )
f2( width = 10 )
f2( )

#error
'''
def f3( *args = 1, **kw = { 'key' = 'value' } ):
    print( args )
    print( kw )

f3( 1, 2, width = 10, height = 20 )
f3( 3, 4, 5, 6, width = 10, height = 20, depth = 30, diension = 5 )
f3( 10 )
f3( width = 10 )
f3( )
'''

def f3( a, *args, **kw ):
    print( a )
    print( args )
    print( kw )

f3( 1, 2, width = 10, height = 20 )
f3( 3, 4, 5, 6, width = 10, height = 20, depth = 30, diension = 5 )
f3( 10 )
f3( 10, width = 10 )
f3( 10, 100, width = 100 )


def h( a, b, c ):
    print( a, b, c )

args = ( 1, 2, 3 )
h( *args )



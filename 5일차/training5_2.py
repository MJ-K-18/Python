def calc_sum( start, end) :
    sum = 0
    for number in range( start, end + 1 ):
        sum += number
    return sum

print ( calc_sum( 1, 10 ) )

def slice_str( string_list ):
    slice_string_list = []
    for string in string_list:
        slice_string_list.append( string[ : 3 ] )
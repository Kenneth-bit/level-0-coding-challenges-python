#!/bin/python3
def max_number(a, b, c):
    ''' Returns the biggest of the three numbers
    '''
    if a > b and a > c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

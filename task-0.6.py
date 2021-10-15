#!/bin/python3
def maximum(a, b, c):
    ''' Returns the biggest of three numbers
    '''
    biggest = 0
    for number in a, b, c:
        if number > biggest:
            biggest = number
        else:
            continue
    print(biggest)


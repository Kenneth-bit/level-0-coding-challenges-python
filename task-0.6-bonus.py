#!/bin/python3
def max_number(*numbers):
    ''' Returns the biggest of three numbers
    '''
    biggest = 0
    for number in numbers:
        if number > biggest:
            biggest = number
        else:
            continue
    print(biggest)


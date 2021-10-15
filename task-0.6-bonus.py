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
max_number(3, 3566, 7891, 7, 9,100)
max_number(6, 2, 450, 4, 86, 345, 7)
max_number(9, 2, 5)

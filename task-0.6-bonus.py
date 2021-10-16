#!/bin/python3
def maximum(*numbers):
    ''' Returns the biggest of three numbers
    '''

    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
        else:
            continue
    print(biggest)

maximum(-5, -7 ,-3, -90)
#!/bin/python3

# Task 0.7 part one
def convert_to_fahrenheit(celcius):
    ''' Converts celcius into fahrenheit degrees
    '''
    fahrenheit = 9/5 * celcius + 32
    print(f"{fahrenheit} F")

# Task 0.7 part two
def convert_to_celcius(fahrenheit):
    ''' Converts fahrenheit into celcius degrees
    '''
    celcius = 5/9 * (fahrenheit - 32)
    print(f"{celcius} C")

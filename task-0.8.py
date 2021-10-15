#!/bin/python3
def make_time(number):
    ''' Converts any number to hours and minutes
    '''
    hr = 0
    m = 0
    # conversion to time
    if number < 60:
        m = number
    elif number >= 60:
        hr = number // 60
        m = number % 60
    
    # plurality checks
    if m != 0 and hr != 0:
        if m > 1 and hr > 1:
            print(f"{hr} hours, {m} minutes")    
        elif m > 1 and hr == 1:
            print(f"{hr} hour, {m} minutes")
        elif m ==1 and hr > 1:
            print(f"{hr} hours {m} minute")
        elif m == 1 and hr == 1:
            print(f"{hr} hour, {m} minute")
    elif m == 0:
        if hr > 1:
            print(f"{hr} hours")
        else:
            print(f"{hr} hour")
    elif hr == 0:
        if m > 1:
            print(f"{m} minutes")
        elif m == 1:
            print(f"{m} minute")

#!/bin/python3
def vowels(string):
    ''' Prints out all the vowels in the string
    '''
    output = []
    vowel_list = 'aeiouAEIOU'
    for letter in string:
        if letter in vowel_list and letter not in output:
            output.append(letter.lower())
            
    print("Vowels: ", end='')
    print(*output, sep=', ')


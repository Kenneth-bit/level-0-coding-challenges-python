#!/bin/python3
def in_common(str1, str2):
    commons = []
    for letter in str1:
        for alphabet in str2:
            if letter == alphabet and letter not in commons:
                commons.append(letter.lower())
    print("Common letters: ")
    print(*commons, sep=', ')

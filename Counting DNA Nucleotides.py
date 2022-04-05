#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:44:36 2022

@author: ryancarrell
"""

#Define exception for strings longer than 1000 nt
class Error(Exception):
    """Base class for other exceptions"""
    pass

class StringTooLong(Error):
    """Raised when string > 1000 nt"""
    pass


#Count number of nucleobases

while True:
    try:
        stringDNA = input('Please enter DNA strand to count nucleobases:')
        if len(stringDNA) > 1000:
            raise StringTooLong()
        else:
            adenineCount = stringDNA.count('A')
            cytosineCount = stringDNA.count('C')
            guanineCount = stringDNA.count('G')
            thymineCount = stringDNA.count('T')
            print(adenineCount, " ", cytosineCount, " ", guanineCount, " ", thymineCount)
        break
    except StringTooLong:
        print("This string exceeds 1000 nt. Please try again.")
        print()
    





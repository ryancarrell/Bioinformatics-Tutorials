#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 15:30:42 2022

@author: ryancarrell
"""

#Define exception for strings longer than 1000 nt
class Error(Exception):
    """Base class for other exceptions"""
    pass

class StringTooLong(Error):
    """Raised when string > 1000 nt"""
    pass


#Transcribe DNA into RNA

while True:
    try:
        stringDNA = input('Please enter DNA strand to count nucleobases:')
        if len(stringDNA) > 1000:
            raise StringTooLong()
        else:
            print(stringDNA.replace('T','U'))
        break
    except StringTooLong:
        print("This string exceeds 1000 nt. Please try again.")
        print()
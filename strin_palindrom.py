#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Filter the string: keep only letters and make them lowercase
    filtered_chars = "".join(char.lower() for char in code if char.isalpha())
    
    # Check if the filtered string is equal to its reverse
    is_palindrome = filtered_chars == filtered_chars[::-1]
    
    # Return 1 for True and 0 for False as required
    return int(is_palindrome)

if __name__ == '__main__':

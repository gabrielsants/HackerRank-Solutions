#Ancestral Name

import math
import os
import random
import re
import sys


#
# Complete the 'sortRoman' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#

def romanToInt(s: str):
    numerals = {
        "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
    }
    output = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and numerals[c] < numerals[s[i+1]]:
            output -= numerals[c]
        else:
            output += numerals[c]
    return output

def sortRoman(names):
    names.sort(key = lambda x: (x.split(" ")[0], romanToInt(x.split(" ")[1]) ))
    return names
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    names_count = int(input().strip())

    names = []

    for _ in range(names_count):
        names_item = input()
        names.append(names_item)

    result = sortRoman(names)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

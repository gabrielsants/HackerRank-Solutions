#Do they belong?

import math
import os
import random
import re
import sys



#
# Complete the 'pointsBelong' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#  5. INTEGER x3
#  6. INTEGER y3
#  7. INTEGER xp
#  8. INTEGER yp
#  9. INTEGER xq
#  10. INTEGER yq
#
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * ( y1 - y2)) / 2.0)

def isTriangleValid(x1, y1, x2, y2, x3, y3):
    A = (
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )
    if A == 0:
        return False
    else:
        return True

def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    
    if(A == A1 + A2 + A3):
        return True
    else:
        return False

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    if(isTriangleValid(x1, y1, x2, y2, x3, y3,) == False):
        return '0'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == True and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == False):
        return '1'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == False and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == True):
        return '2'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == True and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == True):
        return '3'
    elif(isInside(x1, y1, x2, y2, x3, y3, xp, yp) == False and isInside(x1, y1, x2, y2, x3, y3, xq, yq) == False):
        return '4'
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1 = int(input().strip())

    y1 = int(input().strip())

    x2 = int(input().strip())

    y2 = int(input().strip())

    x3 = int(input().strip())

    y3 = int(input().strip())

    xp = int(input().strip())

    yp = int(input().strip())

    xq = int(input().strip())

    yq = int(input().strip())

    result = pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq)

    fptr.write(str(result) + '\n')

    fptr.close()
    
#Cardinality Sorting

import math
import os
import random
import re
import sys


#
# Complete the 'cardinalitySort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def countBits(B):
    count = 0
    while(B):
        if(B & 1):
            count += 1
        B = B>>1
    return count

def insertionSort(nums, aux, n):
    for i in range(1,n,1):
        key1 = aux[i]
        key2 = nums[i]
        j = i -1
        
        while(j >= 0 and aux[j] < key1):
            aux[j+1] = aux[j]
            nums[j+1] = nums[j]
            j = j-1
            
        aux[j+1] = key1
        nums[j+1] = key2
    
    return nums
        
def sortBySetBitCount(nums,n):
    aux = [0 for i in range(n)]
    for i in range(0,n,1):
        aux[i] = countBits(nums[i])
    nums = insertionSort(nums, aux, n)
    x = nums.reverse()
    return nums
        
def cardinalitySort(nums):
    n = len(nums)
    nums = sortBySetBitCount(nums, n)
    return nums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    result = cardinalitySort(nums)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

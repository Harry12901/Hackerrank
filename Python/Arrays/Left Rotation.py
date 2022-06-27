# A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
# For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. 
# Note that the lowest index item moves to the highest index in a rotation. 
# This is called a circular array.

# Given an array a of n integers and a number, d, perform d left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    c = [0]*len(a)
    d = d%len(a)
    if d == 0:
        return a
    for i in range(len(a)):
        c[i] = a[d]
        d+=1
        if(d>=len(a)):
            d=0
    return c

####ALT
# def rotLeft(arr, d):
#     for i in range(d):
#         arr.append(arr[i])

#     for x in arr[d:]:
#         print(x, end=' ')
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

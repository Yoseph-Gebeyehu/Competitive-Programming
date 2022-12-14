#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, a):
    # Write your code here
    for i in range(len(a) - 1 , 0 ,-1):
        value = a[i]
        index = i
        if value < a[i-1]:
            a[i] = a[i-1]
            index -= 1
            for j in range(len(a)):
                print(a[j], end= ' ')
            print()    
        a[index] = value
    for i in range(len(a)):
        print(a[i], end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    insertionSort1(n, a)

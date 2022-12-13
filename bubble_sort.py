#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    numSwap = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - i -1):
            if a[j] > a[j+1]:
                numSwap += 1      
                a[j], a[j+1] = a[j+1], a[j]
    print(f"Array is sorted in {numSwap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a) - 1]}")
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

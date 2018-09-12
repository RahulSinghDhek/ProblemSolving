#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    temp={}
    count=0
    for el in ar:
        temp.setdefault(el,0)
        temp[el]=temp[el]+1
    for k,v in temp.items():
        if v>=2:
            count += int(v/2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

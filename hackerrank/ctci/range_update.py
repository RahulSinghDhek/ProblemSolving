#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    _list = [0]*(n)
    for query in queries:
        _list[query[0]-1] += query[2]
        if query[1] < n:
            _list[query[1]] -= query[2]
    largest_sum=temp=0
    for el in _list:
        temp += el
        largest_sum = max(largest_sum,temp)
    return largest_sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

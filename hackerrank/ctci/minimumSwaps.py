#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    no_of_swaps = 0
    sorted_array =  sorted(arr)
    hash_array = {v:i for i,v in enumerate(arr)}
    for i,v in enumerate(arr):
        correct_value =  sorted_array[i]
        if v != correct_value:
            swap_index = hash_array[correct_value]
            arr[swap_index],arr[i]=arr[i],arr[swap_index]
            hash_array[correct_value],hash_array[v]=i,swap_index
            no_of_swaps +=1
    return no_of_swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

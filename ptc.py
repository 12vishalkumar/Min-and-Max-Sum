import math
import os
import random
import re
import sys
# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    L = len(arr)
    minn = maxx = 0
    for i in range(L-1):
        minn += arr[i]
    for i in range(1,L):
        maxx += arr[i]
    print(minn, maxx)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
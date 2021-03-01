
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sumArr = []
    for i in range(4):
        col = []
        for j in range(4):
            sum = 0
            for k in range(j, j+3):
                sum += arr[i][k]
            sum += arr[i+1][j+1]
            for k in range(j, j+3):
                sum += arr[i+2][k]
            col.append(sum)
        sumArr.append(col)
    maxi = float('-inf') 
    for i in sumArr:
        maxi = max(max(i), maxi)
        # print(maxi)
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)
    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

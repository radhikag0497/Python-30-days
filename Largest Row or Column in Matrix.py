
from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    maxSum = 0
    line = 'row 0 -2147483648'
            
    for i in range(nRows):
        sum = 0
        for j in range(mCols):
            sum = sum + arr[i][j] 
            
        if maxSum < sum:
            maxSum = sum
            line = 'row ' + str(i)
    
    for i in range(mCols):
        sum = 0
        for j in range(nRows):
            sum = sum + arr[j][i]
        if maxSum < sum:
            maxSum = sum
            line = 'column ' + str(i)
    
    if line == 'row 0 -2147483648':
        return line
    else:
        return line + ' ' +str(maxSum)


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    print(findLargest(mat, nRows, mCols))

    t -= 1

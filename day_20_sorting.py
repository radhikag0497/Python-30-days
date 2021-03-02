
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swapCount = 0
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapCount += 1
# if(swapCount == 0):
#     print('')

print('Array is sorted in {} swaps.'.format(swapCount))
# print(a)
print('First Element:', a[0])
print('Last Element:', a[len(a)-1])

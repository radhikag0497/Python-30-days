# Sample Case 1:
# The binary representation of 5(base10) is 101(base2), so the maximum number of consecutive 1's is 1.

# Sample Case 2:
# The binary representation of 13(base10) is 1101(base2), so the maximum number of consecutive 1's is 2.


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    r = []
    while(n > 0):
        r.append(n % 2)
        n = n//2
    
    count = []
    j = 0
    count.append(r[0])
    for i in range(1,len(r)):
        if r[i] == 1:
            count[j]+=1
        else:
            j+=1
            count.append(0)
    
    # print(count)
    print(max(count))

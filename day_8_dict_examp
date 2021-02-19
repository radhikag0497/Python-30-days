# *Input*
# 3 
# sam 99912222 *name and corresponding phone number*
# tom 11122222
# harry 12299933
# *inputs further are a name to look up in the phonebook for corresponding number, if name not found in phn_book, print not found*
# sam
# edward
# harry

# *Output*
# sam=99912222
# Not found
# harry=12299933


import sys
n = int(input())

phone_book = {} # dict initialization
for i in range(n):
    name, no = input().split(' ')
    phone_book.update({name : no})


for line in sys.stdin: # to get input from current line 
    line = line.rstrip('\n') # to remove trailing \n from input keys
    print('{}={}'.format(line,phone_book.get(line))) if line in phone_book else print('Not found')

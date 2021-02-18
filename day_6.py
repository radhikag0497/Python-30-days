# Sample input: 2
#               Hacker
#               Rank
# Sample output : Hce akr
#                 Rn ak

t = int(input())

strg = []
stre = []
stro = []

for i in range(t):
    strg.append(input())

    
for i in range(len(strg)):
    e = ''
    o = ''
    for j in range(len(strg[i])):
        if(j%2 == 0):
            e += strg[i][j]
        else :
            o += strg[i][j]
    stre.append(e)
    stro.append(o)

            
for (j,k) in zip(stre, stro):
    print(j , k)       

def solve(n, k1, k2, w, b):
    grid = []
    white = min(k1,k2)
    white += abs(k1 - k2)/2
    k1 = n - k1
    k2 = n - k2
    black = min(k1,k2)
    black += abs(k1 - k2)/2

    if(white >= w and black >= b):
        return 'YES'
    else:
        return 'NO'

T = int(input('No. of Testcases:'))
for i in range(T):
    n, k1, k2 = list(map(int, input('Enter n, k1, k2 separated by space:').split()))
    w, b = list(map(int, input('Enter w, b separated by space:').split()))
    answer = solve(n, k1, k2, w, b)
    print(answer)

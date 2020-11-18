import sys
input = sys.stdin.readline

def Eratos(n):
    lst = [True]*(n+1)
    
    for i in range(2, int(n**0.5)+1):
        if lst[i] == True:
            for j in range(i+i, n+1, i):
                lst[j] = False
    
    return [i for i in range(2, n+1) if lst[i] == True]

m, n = map(int, input().split(' '))

lst = Eratos(n)

for k in lst:
    if m <= k:
        print(k)

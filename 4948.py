import sys
input = sys.stdin.readline

def Eratos(n):
    lst = [True]*(n+1)
    
    for i in range(2, int(n**0.5)+1):
        if lst[i] == True:
            for j in range(i+i, n+1, i):
                lst[j] = False
    
    return [i for i in range(2, n+1) if lst[i] == True]


while True:
    N = int(input())
    if N == 0 : break
    else:
        set1 = set(Eratos(2*N))
        set2 = set(Eratos(N))
        print(len(set1 - set2))

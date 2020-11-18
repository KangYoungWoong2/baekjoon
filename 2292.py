import sys
input = sys.stdin.readline

N = int(input())

a = 1

if N ==1 : print(1)

else:
    for i in range(1,N+1):
        if (a < N) & (N <= a + 6*i):
            print(i+1)
            break
        else : a = a + 6*i

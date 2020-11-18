import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    H,W,N = map(int, input().split(' '))
    a = 1
    for i in range(1, W+1):
        if (a <= N) & (N < a + H):
            ind = i
            break
        else : a += H
    gap = N - a + 1
    print('{:d}{:02d}'.format(gap,ind))

import sys
input = sys.stdin.readline

A,B,C = map(int, input().replace('\n','').split(' '))


if B >= C :
    print(-1)
else:    
    Q = A//(C-B)
    print(Q+1)

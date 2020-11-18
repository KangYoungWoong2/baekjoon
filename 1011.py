import sys
input = sys.stdin.readline

def minimum(k):
    if k != 1:
        for i in range(1,k):
            if (i**2 < k) & (k <= i**2 + i):
                print(2*i)
                break
            elif (i**2 + i < k) & (k <= i**2 + 2*i + 1):
                print(2*i+1)
                break
            else:
                continue
    else :
        print(1)

T = int(input())

for j in range(T):
    x, y = map(int, input().split(' '))
    minimum(y-x)

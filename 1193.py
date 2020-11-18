import sys
input = sys.stdin.readline

X = int(input())

a = 1
n = 0

for i in range(1, X+1):
    if (a<= X) & (X < a + i):
        n = i
        break
    else:
        a = a + i

gap = X - a

if n%2 == 0:
    print('{}/{}'.format((1+gap), (n-gap)))
else:
    print('{}/{}'.format((n-gap), (1+gap)))
    

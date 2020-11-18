import sys
input = sys.stdin.readline

N = int(input())

impossible = [1,2,4,7]

if N in impossible:
    print(-1)
elif (N == 3) & (N == 5):
    print(1)
elif N == 6:
    print(2)
elif (N-7)%5 == 1:
    print((N-7)//5 + 2)
elif (N-8)%5 == 1:
    print((N-8)//5 + 3)
elif (N-9)%5 == 1:
    print((N-9)//5 + 2)
elif (N-10)%5 ==1:
    print((N-10)//5 + 3)
else:
    print((N-11)//5 + 4)

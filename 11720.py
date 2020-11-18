import sys
input = sys.stdin.readline

N = int(input())
K = list(input().replace('\n', ''))
sum = 0
for i in range(N):
    sum += int(K[i])
print(sum)

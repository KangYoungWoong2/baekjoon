import sys
input = sys.stdin.readline
N = int(input())
for iter in range(N):
  print((N-iter-1)*" " + "*"*(iter+1))
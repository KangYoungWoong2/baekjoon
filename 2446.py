import sys
input = sys.stdin.readline

n = int(input())
for iter in range(n, 0, -1):
  print(" " * (-iter +n) + "*" * (2*iter-1))
for iter in range(2, n+1, 1):
  print(" " * (n-iter) + "*" * (2*iter-1))
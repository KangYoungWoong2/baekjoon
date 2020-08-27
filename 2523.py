import sys
input = sys.stdin.readline

n = int(input())
for iter in range(1,n+1):
  print("*" * iter)
for iter in range(n-1,0,-1):
  print("*" * iter)
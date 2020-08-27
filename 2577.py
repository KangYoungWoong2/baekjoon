import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

value = list(str(A*B*C))

for iter in range(0,10,1):
  print(value.count(str(iter)))
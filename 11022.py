import sys
input = sys.stdin.readline
T = int(input())
for iter in range(T):
  a,b = map(int, input().split(" "))
  print("Case #{}: {} + {} = {}".format(iter+1,a,b,a+b))
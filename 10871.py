import sys
input = sys.stdin.readline
N, X = map(int, input().split(" "))
ar = input().split(" ")
output= ""
for iter in range(N):
  if int(ar[iter]) < X:
    output += ar[iter] + " "
print(output)
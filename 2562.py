import sys
input = sys.stdin.readline
n = 9
list = []
for iter in range(1,n+1,1):
  value = int(input())
  list.append(value)
print(max(list))
print(list.index(max(list))+1)
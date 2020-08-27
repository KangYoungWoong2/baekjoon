import sys
input = sys.stdin.readline

list = []
for iter in range(0, 10, 1):
  list.append(int(input())%42)

count = 0
for iter in range(0, 42, 1):
  if list.count(int(iter)) > 0:
    count += 1

print(count)
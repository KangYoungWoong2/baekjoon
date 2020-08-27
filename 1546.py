import sys
input = sys.stdin.readline

n = int(input())
list = []
list[:n] = map(int, input().split(" "))
M = max(list)

value = 0
for iter in range(0, n, 1):
  value += list[iter]*100/M

print(value/n)
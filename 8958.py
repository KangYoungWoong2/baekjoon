import sys
input = sys.stdin.readline

n = int(input())
k = []
for iter in range(n):
  k.append(input())
  a = k[iter].replace("\n", "")
  a = list(a)
  sum = 0
  x = 0
  for iter2 in range(len(a)):
    if a[iter2] == 'X':
      x = iter2
    if a[iter2] == 'O':
      sum += a[x:iter2+1].count('O')
  print(sum)
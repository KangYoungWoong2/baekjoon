import sys
input = sys.stdin.readline

while True:
  lst = list(map(int, input().split(' ')))
  if min(lst) == 0:break
  c = max(lst)
  lst.remove(c)
  a = lst[0];b=lst[1]
  if c**2 == a**2 + b**2:
    print('right')
  else:
    print('wrong')

import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split(' '))
x2, y2 = map(int, input().split(' '))
x3, y3 = map(int, input().split(' '))

lst_x = [x1, x2, x3]
lst_y = [y1, y2, y3]
a = ''

for x in lst_x:
  if lst_x.count(x) == 1: a += str(x)
for y in lst_y:
  if lst_y.count(y) == 1: a = a + ' ' + str(y)

print(a)

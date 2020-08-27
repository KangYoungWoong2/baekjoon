import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < b and a < c:
  aa = a
elif b < a and b < c:
  aa = b
else:
  aa = c

if d < e:
  bb = d
else:
  bb = e

print(aa + bb - 50)
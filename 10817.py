a, b, c = map(int, input().split(" "))

if a >= b and a >= c:
  if b >= c:
    a1 = a
    a2 = b
    a3 = c
  else:
    a1 = a
    a2 = c
    a3 = b
if b >= a and b >= c:
  if a >= c:
    a1 = b
    a2 = a
    a3 = c
  else:
    a1 = b
    a2 = c
    a3 = a
if c >= a and c >= b:
  if a >= b:
    a1 = c
    a2 = a
    a3 = b
  else:
    a1 = c
    a2 = b
    a3 = a

print(a2)

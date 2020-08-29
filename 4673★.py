def self(n):
  sn = str(n)
  snl = len(sn)
  tmp = []

  for i in range(snl):
    tmp.append(int(sn[i]))
  
  return sum(tmp) + n

arr = []

for i in range(10000):
  arr.append(self(i))
for i in range(10000):
  if i in arr:
    pass
  else:
    print(i)


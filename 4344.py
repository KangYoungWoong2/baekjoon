n = int(input())
for iter in range(n):
  k = list(map(int, input().split()))
  average = (sum(k) - k[0])/k[0]
  counter = 0
  for iter3 in range(len(k)-1):
    if k[iter3+1] > average:
      counter += 1
  ratio = counter * 100 / k[0]
  print ("%.3f%%" % ratio)
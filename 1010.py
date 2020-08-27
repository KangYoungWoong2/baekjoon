import sys
input =sys.stdin.readline
N = int(input())
if N <10:
  N0 = str(N)
  N1 = "0" + N0

else:
  N1 = str(N)

counter = 0
switch = 1
while switch == 1 :
  N2 = int(N1[0]) + int(N1[1])
  if N2<10:
    N3 = int(N1[1])*10 + N2
    counter +=1
  elif N2>=10:
    N2 = str(N2)
    N3 = int(N1[1])*10 + int(N2[1])
    N3 = int(N3)
    counter +=1
  
  if N3 == N:
    switch = 0
  elif N3 < 10:
    N1 = "0"+str(N3)
  elif N3 >=10:
    N1 = str(N3)

print(counter)
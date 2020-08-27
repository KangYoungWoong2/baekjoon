import sys
input = sys.stdin.readline

n = int(input())
for iter in range(1, n+1, 1):
  for iter in range(1, n+1, 1):
    string1 = "* "
    if n != 1 :
      string1 *= (n+1)//2
    
    string2 = " *"
    string2 *= n//2
  
  if n == 1:
    print(string1)
  else:
    print(string1)
    print(string2)
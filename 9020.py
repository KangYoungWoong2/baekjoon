import sys
input = sys.stdin.readline

T = int(input())
def Eratos(n):
    lst = [True]*(n+1)
    
    for i in range(2, int(n**0.5)+1):
        if lst[i] == True:
            for j in range(i+i, n+1, i):
                lst[j] = False
    
    return [i for i in range(2, n+1) if lst[i] == True]

prime = Eratos(10000) 

for _ in range(T):
  n = int(input())
  if n/2 in prime:
    print(int(n/2),int(n/2))
  else:
    for i in range(1,int(n/2+1)):
      if (int(n/2 +i)) in prime and (int(n/2 - i)) in prime:
        print(int(n/2 -i), int(n/2+i))
        break

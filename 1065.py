import sys
input = sys.stdin.readline

def hannum(N):
    if N < 10 :
        return True
        
    elif N < 100 :
        a = N//10
        b = (N - 10*a)
        return True
    
    elif N < 1000:
        a = N//100
        b = (N - 100*a)//10
        c = (N - 100*a - 10*b)
        if (a-b) == (b-c):
            return True
        else:
            return False
    else:
        return False
    
  
K = int(input())
lst = list()
for i in range(1,K+1):
    s = hannum(i)
    if s == True:
        lst.append(i)
        
print(len(lst))

import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

def prime(n):
    if n in [2,3,5,7]:
        return True
    elif (n % 2 == 0):
        return False
    elif n%5 == 0 :
        return False
    else:
        for i in range(3,n):
            if n%i == 0:
                return False
                break
            if i == n-1:
                return True

counter = 0
lst = []

for i in range(M,N+1):
    boolean = prime(i)
    if boolean == True:
        lst.append(i)
    
if len(lst) != 0:    
    print(sum(lst))
    print(min(lst))
else:
    print(-1)

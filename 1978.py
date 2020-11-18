import sys
input = sys.stdin.readline

N = int(input())
string = input().replace('\n','')
lst = list(map(int, string.split(' ')))

def prime(n):
    if n in [2,3,5,7]:
        return True
    elif (n != 2) & (n % 2 == 0):
        return False
    elif n%5 ==0 :
        return False
    else:
        for i in range(3,n):
            if n%i == 0:
                return False
                break
            if i == n-1:
                return True

counter = 0
for i in lst:
    boolean = prime(i)
    if boolean == True:
        counter += 1
print(counter)

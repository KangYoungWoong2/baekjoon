import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a, b = map(str, input().replace('\n', '').split(' '))
    a = int(a)
    lst1 = list(b)
    
    lst2 = lst1.copy()
    for i in range(len(lst1)):
       for _ in range(a-1):
           lst2[i] += lst1[i]
    
    s = ''.join(lst2)
    print(s)

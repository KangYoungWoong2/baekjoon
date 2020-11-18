import sys
input = sys.stdin.readline

s = input().replace('\n', '')
s = s.lower()

lst1 = list(s)
lst2 = []
lst3 = list(set(lst1))

for i in lst3:
    lst2.append(lst1.count(i))

if lst2.count(max(lst2)) > 1:
    print('?')
else:
    a = lst3[lst2.index(max(lst2))]
    a = a.upper()
    print(a)

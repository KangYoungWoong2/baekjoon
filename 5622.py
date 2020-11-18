import sys
input = sys.stdin.readline


s = input().replace('\n','')
s = list(s)

lst = []

for i in s:
    if (ord(i) - 65)//3 == 0:
        lst.append(2)
    elif (ord(i) - 65)//3 == 1:
        lst.append(3)
    elif (ord(i) - 65)//3 == 2:
        lst.append(4)
    elif (ord(i) - 65)//3 == 3:
        lst.append(5)
    elif (ord(i) - 65)//3 == 4:
        lst.append(6)
    elif ord(i)//4 == 20:
        lst.append(7)
    elif (ord(i) - 66)//3 == 6:
        lst.append(8)
    else:
        lst.append(9)
        
print(sum(lst)+len(lst))

import sys
input = sys.stdin.readline

N = int(input())
lst = []

for i in range(N):
    a = str(input().replace('\n',''))
    lst.append(a)

count = 0

for i in range(len(lst)):
    lst_string = list(lst[i])
    if len(lst_string) > len(set(lst_string)):
        lst_set = []
        for s in lst_string:
            if lst_string.count(s) > 1 : lst_set.append(s)
        counter = 0
        for k in lst_set:
            ind = lst_string.index(k)
            n = lst_string.count(k)
            for t in range(n-1):
                if lst_string[ind] != lst_string[ind+t+1]:
                    counter += 1
                
        if counter == 0: 
            count += 1

    else:
        count += 1
                
print(count)

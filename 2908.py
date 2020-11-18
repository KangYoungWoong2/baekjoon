import sys
input = sys.stdin.readline


a, b = map(str, input().replace('\n','').split(' '))

a = list(a)
b = list(b)

a = int(a[2]) * 100 + int(a[1]) * 10 + int(a[0])
b = int(b[2]) * 100 + int(b[1]) * 10 + int(b[0])

lst = [a, b]
print(max(lst))

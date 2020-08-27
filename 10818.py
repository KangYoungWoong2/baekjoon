import sys
input = sys.stdin.readline
n = int(input())
list=[]
list[:n] = map(int, input().split(" "))
print(min(list), max(list))
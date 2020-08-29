import sys
input = sys.stdin.readline

def solve(a: list):
  sum = 0
  for iter in a:
    sum += iter
  return sum
  print(sum)
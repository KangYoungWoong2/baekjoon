import sys
input = sys.stdin.readline
import math

counter = 0
line = '***\n* *\n***'

def fstar(counter, n, line):
  counter += 1
  if counter == round(math.log(n,3)):
    print(line)
    return
  else:
    lst = line.split('\n')
    k = 3**(counter+1)
    newlst = [0]*int(2*k/3)
    for i in range(int(k/3)):
      newlst[i] = lst[i%(3**counter)]*3
    for j in range(int(k/3),int(2*k/3)):
      newlst[j] = lst[j%(3**counter)] + lst[j%(3**counter)].replace('*',' ') + lst[j%(3**counter)]
    line = '\n'.join(newlst)
    line += '\n' + '\n'.join(newlst[:int(k/3)])
    return fstar(counter=counter, n=n, line=line)

n = int(input())

fstar(counter,n,line)

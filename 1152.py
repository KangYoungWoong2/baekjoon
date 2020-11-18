import sys
input = sys.stdin.readline

import re

s = input().replace('\n', '')
s = s.split(' ')

for i in range(len(s)):
    s[i] = re.sub('[^a-zA-Z]','',s[i])

for i in range(s.count('')):
    s.remove('')
    
print(len(s))

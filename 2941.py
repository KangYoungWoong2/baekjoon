import sys
input = sys.stdin.readline


s = input().replace('\n','')
s = list(s)
lst = []

kroatia = ['-','=','j']
for i in range(len(s)) :
    if s[i] not in kroatia:
        lst.append(s[i])
    elif s[i] =='-':
        pass
    elif s[i] == '=':
        if (s[i-1] == 'c') or (s[i-1] == 's'):
            pass
        elif (s[i-1] == 'z') and (s[i-2] == 'd'):
            lst.remove('z')
        else:
            pass
    elif s[i] == 'j':
        if s[i-1] in ['n','l']:
            pass
        else:
            lst.append('j')



print(len(lst))

import sys
input = sys.stdin.readline

dct = {'a':-1, 'b':-1, 'c':-1, 'd':-1,'e':-1,'f':-1,'g':-1,'h':-1,'i':-1,'j':-1,'k':-1,'l':-1,'m':-1,'n':-1,'o':-1,'p':-1,'q':-1,'r':-1,'s':-1,'t':-1,'u':-1,'v':-1,'w':-1,'x':-1,'y':-1,'z':-1}


s = input().replace('\n', '')
lst = list(s)

for i,j in enumerate(lst):
    if j in lst[:i]:
        pass
    else:
        dct[j] = i

lst = []
lst_dct = list(dct.values())
for i in range(len(dct)):
    lst.append(str(lst_dct[i]))

a = ' '.join(lst)
print(a)

import sys
input = sys.stdin.readline

A = 1+2
B = A+3
C = B+4
D = C+5
E = D+6
F = E+7
G = F+8
H = G+9
I = H+10
J = I+11
K = J+12
L = K+13
M = L+14
N = M+15

zero_floor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
first_floor = [1,A,B,C,D,E,F,G,H,I,J,K,L,M,N]

matrix = []
matrix.append(zero_floor)
matrix.append(first_floor)
lst = []

for k in range(2, 15):
    for n in range(2,15):
        if len(lst) == 0:
            lst = [1]
        else:pass
    
        value = 0
        for s in range(n):
            value += matrix[k-1][s]
        lst.append(value)
    matrix.append(lst)
    lst = []

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(matrix[k][n-1])
        

from math import log10, ceil, sqrt

T = int(input())
while (T>0):
    T -= 1
    PHI = (1+sqrt(5))/2 
    print(int(ceil((int(input())-1 + log10(5)/2) / log10(PHI))))

from math import factorial as fact

for i in range(int(input())):
    m, n = [int(j) for j in input().split(" ")]
    print((fact(m + n) // (fact(m) * fact(n))) % 1000000007)

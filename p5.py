from fractions import gcd

val = [1,2,6]
for i in range(4, 41):
    hcf = gcd(val[-1], i)
    hcf = i//hcf
    val.append(hcf*val[-1])

#print(val[:11])
for _ in range(int(input())):
    n = int(input())
    print(val[n-1])

import math

def largest(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n //= i
    if n > 2:
        maxPrime = n
     
    return int(maxPrime)
    
for _ in range(int(input())):
    n = int(input())
    ans = largest(n)
    print(ans)

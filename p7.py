prime = [True]*(10**6)
primes = []

for i in range(2, 10**6):
    if prime[i]:
        primes.append(i)
        for j in range(2*i, 10**6, i):
            prime[j]=False

for _ in range(int(input())):
    print(primes[int(input())-1])

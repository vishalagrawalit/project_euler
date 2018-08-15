prime = [True]*(10**6+5)
primes = []

x = -1
summation = 0
for i in range(2, 10**6+5):
    if prime[i]:
        x+=1
        prime[i] = (True, x)
        summation += i
        primes.append(summation)
        for j in range(2*i, 10**6+5, i):
            prime[j]=False
    else:
        prime[i] = (False, x)

for _ in range(int(input())):
    n = int(input())
    index = prime[n][1]
    #print(index)
    print(primes[index])

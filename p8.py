for _ in range(int(input())):
    x = input().split()
    n,k = int(x[0]),int(x[1])
    number = input()
    maxi = 0
    for i in range(n-k):
        res = 1
        for j in range(i,i+k):
            res *= int(number[j])
        if res > maxi:
            maxi = res
    print(maxi)

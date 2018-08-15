for _ in range(int(input())):
    n = int(input())
    flag = 1
    maxi = -1
    for i in range(1, int(n/3)+1):
        b = (n*n - 2*n*i)//(2*n - 2*i)
        c = n-i-b
        if i*i + b*b == c*c:
            maxi = max(maxi, i*b*c)
    print(maxi)

for _ in range(int(input())):
    n = int(input())
    i,j=1,1
    res = 0
    while i+j<n:
        i, j = j, i+j
        if j&1==0:
            res+=j
    print(res)

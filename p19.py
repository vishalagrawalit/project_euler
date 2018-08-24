d = dict()
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(i+1):
            d[(i,j)] = arr[j]

# print(d)

    ans = 0
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            maxi = max(d[(i+1, j)], d[(i+1, j+1)])
            d[(i, j)] += maxi

    # print(d)
    print(d[(0,0)])

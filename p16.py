for _ in range(int(input())):
    n = int(input())
    s = str(2**n)
    ans = 0
    for i in range(len(s)):
        ans+=int(s[i])
    print(ans)

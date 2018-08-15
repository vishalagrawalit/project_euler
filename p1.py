for _ in range(int(input())):
    n = int(input())
    fif = (n-1)//15
    five = (n-1)//5
    three = (n-1)//3
    
    ans = ((three*(three+1)*3)//2) + ((five*(five+1)*5)//2) - ((fif*(fif+1)*15)//2)
    print(ans)

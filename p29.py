def checks(l,h,d) :
    tot=0
    for i in range(l,h) :
        temp=i
        s=0
        while(temp>0) :
            s += (temp%10)**d
            temp //= 10
        if s == i :
            tot += s         
    return tot
    
n = int(input())   
if n==3 :
    print(checks(100,1000,3))
elif n==4 :
    print(checks(1000,10000,4))
elif n==5 :
    print(checks(10000,100000,5))
elif n==6 :
    print(checks(100000,1000000,6))

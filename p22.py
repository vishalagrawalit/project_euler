d = dict()

names = []
for i in range(int(input())):
    s = input()
    names.append(s)

names.sort()

i = 0
for s in names:
    val = 0
    for j in s:
        val += ord(j)-64
    i+=1
    d[s] = val*i    
    
for _ in range(int(input())):
    print(d[input()])

first = [1, 210, 40755, 7906276, 1533776805, 297544793910, 57722156241751]
second = [1, 40755, 1533776805, 57722156241751]

arr = list(map(int, input().split()))

if arr[1]==3:
    count = 0
    for i in first:
        if i < arr[0]:
            count+=1
    for i in range(count):
        print(first[i])
else:
    count = 0
    for i in second:
        if i < arr[0]:
            count+=1
    for i in range(count):
        print(second[i])

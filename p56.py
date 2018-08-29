n = int(input())
print(max([sum(map(int, str(i**j))) for i in range(2, n) for j in range(2, n)]))

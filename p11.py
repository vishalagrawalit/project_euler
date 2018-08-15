mat = []
for i in range(20):
    arr = list(map(int, input().split()))
    mat.append(arr)

maxi = 0
for i in range(20):
    for j in range(20):
        if i-1>=0 and i-2>=0 and i-3>=0:
            val = mat[i][j]*mat[i-1][j]*mat[i-2][j]*mat[i-3][j]
            maxi = max(maxi, val)
        if i+1<20 and i+2<20 and i+3<20:
            val = mat[i][j]*mat[i+1][j]*mat[i+2][j]*mat[i+3][j]
            maxi = max(maxi, val)
        if j+1<20 and j+2<20 and j+3<20:
            val = mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3]
            maxi = max(maxi, val)
        if j-1>=0 and j-2>=0 and j-3>=0:
            val = mat[i][j]*mat[i][j-1]*mat[i][j-2]*mat[i][j-3]
            maxi = max(maxi, val)
        if i-1>=0 and i-2>=0 and i-3>=0 and j-1>=0 and j-2>=0 and j-3>=0:
            val = mat[i][j]*mat[i-1][j-1]*mat[i-2][j-2]*mat[i-3][j-3]
            maxi = max(maxi, val)
        if i-1>=0 and i-2>=0 and i-3>=0 and j+1<20 and j+2<20 and j+3<20:
            val = mat[i][j]*mat[i-1][j+1]*mat[i-2][j+2]*mat[i-3][j+3]
            maxi = max(maxi, val)
        if i+1<20 and i+2<20 and i+3<20 and j-1>=0 and j-2>=0 and j-3>=0:
            val = mat[i][j]*mat[i+1][j-1]*mat[i+2][j-2]*mat[i+3][j-3]
            maxi = max(maxi, val)
        if i+1<20 and i+2<20 and i+3<20 and j+1<20 and j+2<20 and j+3<20:
            val = mat[i][j]*mat[i+1][j+1]*mat[i+2][j+2]*mat[i+3][j+3]
            maxi = max(maxi, val)
print(maxi)

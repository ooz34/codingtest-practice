n = int(input())
m = int(input())
snail=[[0]*n for _ in range(n)]
num = n*n
i, j = 0, 0
my, mx = 0, 0
direc = [(1,0), (0,1), (-1,0), (0,-1)]
d = 0
while num > 0:
    snail[i][j] = num
    if num == m:
        my, mx = i+1, j+1
    if not (0<= i+direc[d][0]<n) or not (0<= j+direc[d][1]<n) or snail[i+direc[d][0]][j+direc[d][1]]:
        d = (d+1)%4
    i += direc[d][0]
    j += direc[d][1]
    num -= 1

for row in snail:
    print(*row)
print(my, mx)
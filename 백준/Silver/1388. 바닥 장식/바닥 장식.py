import sys
n, m = map(int, sys.stdin.readline().split())
floor = []
for _ in range(n):
    floor.append(list(sys.stdin.readline().strip()))

def dfs(deco, i, j):
    floor[i][j] = 0
    if deco == '-':
        for dy in [-1, 1]:
            y = j + dy
            if (0 < y < m) and floor[i][y] == '-':
                dfs('-', i, y)
    if deco == '|':
        for dx in [-1, 1]:
            x = i + dx
            if 0 < x < n and floor[x][j] == '|':
                dfs('|', x, j)
    
cnt = 0
for i in range(n):
    for j in range(m):
        deco = floor[i][j]
        if deco:
            dfs(deco, i, j)
            cnt += 1
print(cnt)
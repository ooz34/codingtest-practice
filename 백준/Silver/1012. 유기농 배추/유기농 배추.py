import sys
from collections import deque
t = int(sys.stdin.readline().strip())
xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(graph, x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = 0
    while q:
        qx, qy = q.popleft()
        for dx, dy in xy:
            nx = qx + dx
            ny = qy + dy
            if 0 <= nx < m and 0 <= ny <n and graph[nx][ny]:
                q.append([nx, ny])
                graph[nx][ny] = 0
                
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    
    patch = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        patch[x][y] = 1
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if patch[i][j]:
                bfs(patch, i, j)
                cnt += 1
    print(cnt)
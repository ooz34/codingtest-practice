import sys
from collections import deque
def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    v[x][y] = 1
    while q:
        qx, qy = q.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = qx + dx, qy + dy
            if 0<= nx <n and 0<= ny < n and not v[nx][ny] and graph[nx][ny] > h:
                q.append((nx, ny))
                v[nx][ny] = 1
                
n = int(sys.stdin.readline().rstrip())
graph = []
heights = set([0]) 
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    heights.update(row)

ans = 0
for h in sorted(heights):
    cnt = 0
    v = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not v[i][j]:
                cnt += 1
                bfs(i, j, h)
    ans = max(ans, cnt)
print(ans)
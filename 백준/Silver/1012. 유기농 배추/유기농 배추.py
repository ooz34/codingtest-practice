import sys
from collections import deque
def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        nx, ny = q.popleft()
        for dx, dy in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            qx, qy = nx + dx, ny + dy
            if 0 <= qx < m and 0 <= qy <n and graph[qx][qy]:
                q.append((qx, qy))
                graph[qx][qy] = 0
tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    m, n, k = map(int, sys.stdin.readline().split())
    
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j]:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)
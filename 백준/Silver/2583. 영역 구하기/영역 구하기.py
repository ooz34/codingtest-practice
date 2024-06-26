import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())
graph = [[1]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

areas = []
q = deque()
for x in range(m):
    for y in range(n):
        if graph[x][y]:
            area = 0
            q.append((x, y))
            graph[x][y] = 0
            while q:
                qx, qy = q.popleft()
                area += 1
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = qx + dx, qy + dy
                    if 0<= nx < m and 0<= ny <n and graph[nx][ny]:
                        graph[nx][ny] = 0
                        q.append((nx, ny))
            areas.append(area)
areas.sort()
print(len(areas))
print(*areas)     
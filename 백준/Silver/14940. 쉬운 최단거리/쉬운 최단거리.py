import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [[-1]*m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append([i, j])
            visited[i][j] = 0
            break
    if q:
        break

xy = [[-1,0], [1,0], [0,-1], [0,1]]

while q:
    x, y = q.popleft()
    for dx, dy in xy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
            if graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
            elif graph[nx][ny] == 0:
                visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
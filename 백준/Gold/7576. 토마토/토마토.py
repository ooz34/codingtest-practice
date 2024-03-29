import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

xy = [(1,0), (0,1), (-1,0), (0,-1)]
riped = [[0]*M for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            queue.append((i, j))
            continue
        if not box[i][j]:
            riped[i][j] = -1

while queue:
    x, y = queue.popleft()
    for dx, dy in xy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not box[nx][ny] and riped[nx][ny]==-1:
            queue.append((nx, ny))
            riped[nx][ny] = riped[x][y] + 1
                
day = 0
for row in riped:
    day = max(day, max(row))
    if -1 in row:
        print(-1)
        break
else:
    print(day)
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
maze = [list(input().strip()) for _ in range(R)]

xy = [(1,0), (0,1), (-1,0), (0,-1)]

dist_fire = [[-1] * C for _ in range(R)]
dist_jihoon = [[-1] * C for _ in range(R)]

queue_fire = deque()
queue_jihoon = deque()

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            queue_fire.append((i, j))
            dist_fire[i][j] = 0
        elif maze[i][j] == 'J':
            queue_jihoon.append((i, j))
            dist_jihoon[i][j] = 0

while queue_fire:
    x, y = queue_fire.popleft()
    for dx, dy in xy:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if dist_fire[nx][ny] >= 0 or maze[nx][ny] == '#':
            continue
        dist_fire[nx][ny] = dist_fire[x][y] + 1
        queue_fire.append((nx, ny))

while queue_jihoon:
    x, y = queue_jihoon.popleft()
    for dx, dy in xy:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            print(dist_jihoon[x][y] + 1)
            exit()
        if dist_jihoon[nx][ny] >= 0 or maze[nx][ny] == '#':
            continue
        if dist_fire[nx][ny] != -1 and dist_fire[nx][ny] <= dist_jihoon[x][y] + 1:
            continue
        dist_jihoon[nx][ny] = dist_jihoon[x][y] + 1
        queue_jihoon.append((nx, ny))

print("IMPOSSIBLE")
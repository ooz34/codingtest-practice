import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    queue = deque()
    queue.append(((x, y)))
    distance = [[-1]*M for _ in range(N)]
    distance[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in xy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] and distance[nx][ny]==-1:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
    return distance[N-1][M-1]

print(bfs(0,0))
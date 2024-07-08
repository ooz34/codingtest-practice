import sys
from collections import deque
n, l, r = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(x, y, v):
    global is_moved
    q = deque()
    q.append((x, y))
    popul = 0
    united = []
    while q:
        qx, qy = q.popleft()
        v[qx][qy] = 1
        p1 = graph[qx][qy]
        united.append((qx, qy))
        popul += p1
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = qx+dx, qy+dy
            if 0<= nx <n and 0<= ny <n and not v[nx][ny]:
                p2 = graph[nx][ny]
                if l<= abs(p1-p2) <=r:
                    q.append((nx, ny))
                    v[nx][ny] = 1
    if len(united) > 1:
        temp = popul//len(united)
        for ux, uy in united:
            graph[ux][uy] = temp
            is_moved = 1

days = 0
while True:
    v=[[0]*n for _ in range(n)]
    is_moved = 0
    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                bfs(i, j, v)
    if not is_moved:
        break
    days += 1

print(days)
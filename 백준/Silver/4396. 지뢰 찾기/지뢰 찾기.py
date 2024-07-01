import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
v = []
for _ in range(n):
    v.append(list(sys.stdin.readline().rstrip()))
xy = [(-1,-1), (0,-1), (1,-1), (-1, 0), (1, 0), (-1,1), (0,1), (1,1)]

ans = [['.']*n for _ in range(n)]
is_fail = False
for i in range(n):
    for j in range(n):
        if v[i][j] == 'x':
            if graph[i][j] == '*':
                is_fail = True
            cnt = 0
            for dx, dy in xy:
                nx, ny = i+dx, j+dy
                if 0<= nx < n and 0<= ny < n and graph[nx][ny] == '*':
                   cnt += 1
            ans[i][j] = str(cnt)
            
if is_fail:
    for i, row in enumerate(graph):
        for j, val in enumerate(row):
            if val == '*':
                ans[i][j] = '*'

for row in ans:
    print(''.join(row))
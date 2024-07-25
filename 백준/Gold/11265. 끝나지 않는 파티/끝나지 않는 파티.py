import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')
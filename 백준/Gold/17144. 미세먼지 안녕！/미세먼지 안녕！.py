import sys
r, c, t = map(int, sys.stdin.readline().split())
graph = []
ap = 0
for i in range(r):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    if not ap:
        for a in row:
            if a == -1:
                ap = i
                break
up_ap = ap
down_ap = ap + 1

def spread_and_purify():
    global graph
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    spread = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                amount = graph[i][j] // 5
                count = 0
                for dx, dy in directions:
                    nx, ny = j + dx, i + dy
                    if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] != -1:
                        spread[ny][nx] += amount
                        count += 1
                graph[i][j] -= amount * count

    for i in range(r):
        for j in range(c):
            graph[i][j] += spread[i][j]

    for i in range(up_ap - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    for j in range(c - 1):
        graph[0][j] = graph[0][j + 1]
    for i in range(up_ap):
        graph[i][c - 1] = graph[i + 1][c - 1]
    for j in range(c - 1, 1, -1):
        graph[up_ap][j] = graph[up_ap][j - 1]
    graph[up_ap][1] = 0

    for i in range(down_ap + 1, r - 1):
        graph[i][0] = graph[i + 1][0]
    for j in range(c - 1):
        graph[r - 1][j] = graph[r - 1][j + 1]
    for i in range(r - 1, down_ap, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    for j in range(c - 1, 1, -1):
        graph[down_ap][j] = graph[down_ap][j - 1]
    graph[down_ap][1] = 0

for _ in range(t):
    spread_and_purify()

ans = sum(sum(row) for row in graph) + 2
print(ans)

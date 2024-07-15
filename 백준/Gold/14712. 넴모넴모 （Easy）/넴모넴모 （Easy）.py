def dfs(x, y):
    global cnt
    if (x, y) == (1, n+1):
        cnt += 1
        return
    if x==m:
        nx, ny = 1, y+1
    else:
        nx, ny = x+1, y
    # 놓지 않은 경우
    dfs(nx, ny)
    # 놓은 경우
    if not graph[y][x-1] or not graph[y-1][x-1] or not graph[y-1][x]:
        graph[y][x] = 1
        dfs(nx, ny)
        graph[y][x] = 0

n, m = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
cnt = 0
dfs(1,1)
print(cnt)
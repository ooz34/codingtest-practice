import sys
n, k = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i, [w, v] in enumerate(items):
    for j in range(1, k+1):
        if w>j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w] + v)
print(dp[n][k])

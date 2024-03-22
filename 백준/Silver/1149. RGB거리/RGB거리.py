import sys

N = int(sys.stdin.readline())
dp = [[0, 0, 0]]
for _ in range(N):
  dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]
    
print(min(dp[N][0], dp[N][1], dp[N][2]))
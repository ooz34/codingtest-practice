n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(2, n+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[i-j] + dp[j] + j*(i-j))
print(dp[-1])
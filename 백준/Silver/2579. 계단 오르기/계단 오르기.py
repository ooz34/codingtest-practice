import sys

n = int(sys.stdin.readline())
steps = [0]
for _ in range(n):
  steps.append(int(sys.stdin.readline()))

# dp[i][j]: 연속하여 밟은 계단이 j개이고, i번째 계단까지 올랐을 때, 얻을 수 있는 점수의 최댓값 
dp = [[0 for col in range(3)] for row in range(n+1)]
dp[1][1] = steps[1]
if n > 1:
    dp[2][1] = steps[2]
    dp[2][2] = steps[1] + steps[2]

for k in range(3, n+1):
    dp[k][1] = max(dp[k-2][1], dp[k-2][2]) + steps[k]
    dp[k][2] = dp[k-1][1] + steps[k]

print(max(dp[n][1], dp[n][2]))
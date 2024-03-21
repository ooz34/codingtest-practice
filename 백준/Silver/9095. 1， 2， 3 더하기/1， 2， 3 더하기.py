import sys
T = int(sys.stdin.readline())
tc = []
for _ in range(T):
  tc.append(int(sys.stdin.readline()))

# dp[i]: 1, 2, 3의 합으로 나타내는 방법의 수
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

dp = [0, 1, 2, 4] + [0]*7

for i in range(4, 11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in tc:
  print(dp[n])
import sys
N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]
answer = []

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

idx = N    
while idx > 0:
    answer.append(idx)
    if idx % 3 == 0 and dp[idx//3] == dp[idx] - 1:
        idx //= 3
    elif idx % 2 == 0 and dp[idx//2] == dp[idx] - 1:
        idx //= 2
    else:
        idx -= 1

print(dp[N])
print(' '.join(map(str, reversed(answer[::-1]))))
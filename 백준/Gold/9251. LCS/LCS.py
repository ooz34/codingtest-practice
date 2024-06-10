str1 = list(input())
str2 = list(input())

dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
for i, ch1 in enumerate(str1, start=1):
    for j,ch2 in enumerate(str2, start=1):
        if ch1==ch2:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(str1)][len(str2)])
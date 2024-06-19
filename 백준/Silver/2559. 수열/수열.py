import sys
n, k = map(int, sys.stdin.readline().split())
tlist = list(map(int, sys.stdin.readline().split()))

part_sum = [0]*(n-k+1)
for i in range(k):
    part_sum[0] += tlist[i]
    
ans = part_sum[0]  
for i in range(1, n-k+1):
    part_sum[i] = part_sum[i-1] - tlist[i-1] + tlist[i+k-1]
    ans = max(ans, part_sum[i])

print(ans)
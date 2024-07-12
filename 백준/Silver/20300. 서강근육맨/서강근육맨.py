import sys
n = int(sys.stdin.readline().rstrip())
tlist = sorted(map(int, sys.stdin.readline().split()))

ans = 0
if n & 1:
    ans = tlist[-1]
    for i in range(n//2):
        ans = max(ans, tlist[i] + tlist[n-2-i])
else:
    for i in range(n//2):
        ans = max(ans, tlist[i] + tlist[n-1-i])
        
print(ans)

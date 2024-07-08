import sys
n, m, l = map(int, sys.stdin.readline().split())
loc = [0] + list(map(int, sys.stdin.readline().split())) + [l]
loc.sort()

st, ed = 1, l-1
ans = 0
while st <= ed:
    cnt = 0
    mid = (st+ed)//2
    for i in range(1, len(loc)):
        if loc[i] - loc[i-1] > mid:
           cnt += (loc[i] - loc[i-1] -1)//mid
    if cnt > m:
        st = mid+1
    else:
        ed = mid-1
        ans = mid
print(ans)
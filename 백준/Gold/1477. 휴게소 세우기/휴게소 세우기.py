import sys
from bisect import insort_left
n, m, l = map(int, sys.stdin.readline().split())
loc = [0] + list(map(int, sys.stdin.readline().split())) + [l]
loc.sort()

st = 1
en = l-1
answer = 0
while st <= en:
    cnt = 0
    mid = (st + en)//2
    for i in range(1, len(loc)):
        if loc[i] - loc[i-1] > mid:
            cnt += (loc[i] - loc[i-1] -1)//mid
    if cnt > m:
        st = mid + 1
    else:
        en = mid - 1
        answer = mid
print(answer)
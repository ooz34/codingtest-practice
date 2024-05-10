import sys
from bisect import bisect_left
k, n = map(int, sys.stdin.readline().split())
lengths = sorted([int(sys.stdin.readline()) for _ in range(k)])

st = 1
en = lengths[-1]
while st <= en:
    mid = (st + en)//2
    cnt = 0
    for lan in lengths:
        cnt += lan//mid
    if cnt >= n:
        st = mid + 1
    else:
        en = mid - 1
print(en)
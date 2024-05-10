import sys
from bisect import bisect
n, k = map(int, sys.stdin.readline().split())
fv = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0
while k:
    coin = fv[bisect(fv, k)-1]
    curr_cnt = k//coin
    cnt += curr_cnt
    k -= coin*curr_cnt
print(cnt)
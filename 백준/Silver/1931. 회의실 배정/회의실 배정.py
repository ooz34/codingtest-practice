import sys
from bisect import bisect
n = int(sys.stdin.readline().strip())
meetings = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key = lambda x: [x[1], x[0]])

cnt = 0
t = 0
for st, en in meetings:
    if st >= t:
        cnt += 1
        t = en
print(cnt)
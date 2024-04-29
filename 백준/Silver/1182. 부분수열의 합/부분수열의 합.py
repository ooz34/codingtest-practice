import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(1, n + 1):
    for subseq in combinations(seq, i):
        if sum(subseq) == s:
            cnt += 1

print(cnt)
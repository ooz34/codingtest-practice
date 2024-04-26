import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
nlist = sorted(map(int, sys.stdin.readline().split()))

for p in sorted(set(combinations(nlist, m))):
    print(*p)
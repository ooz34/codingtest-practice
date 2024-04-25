import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))

for p in combinations(nlist, m):
    print(*p)
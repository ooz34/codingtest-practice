import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))

for p in combinations_with_replacement(nlist, m):
    print(*p)
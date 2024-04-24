import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

for p in combinations(list(range(1, n+1)), m):
    print(*p)
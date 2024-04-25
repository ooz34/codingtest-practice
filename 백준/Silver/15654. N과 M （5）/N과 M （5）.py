import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))

for p in permutations(nlist, m):
    print(*p)
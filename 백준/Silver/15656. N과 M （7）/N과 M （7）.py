import sys
from itertools import product
n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))

for p in product(nlist, repeat=m):
    print(*p)
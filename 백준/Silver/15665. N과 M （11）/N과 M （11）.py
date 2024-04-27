import sys
from itertools import product
n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

for p in sorted(set(product(nlist, repeat=m))):
    print(*p)
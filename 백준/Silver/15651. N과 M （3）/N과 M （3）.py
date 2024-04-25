import sys
from itertools import product 

n, m = map(int, sys.stdin.readline().split())

for p in product(list(range(1, n+1)), repeat=m):
    print(*p)
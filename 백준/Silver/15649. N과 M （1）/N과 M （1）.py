import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

for p in permutations(list(range(1, n+1)), m):
    print(' '.join(str(num) for num in p))
import sys
from collections import Counter
n, c = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
counter = Counter(arr)
for k, v in sorted(counter.items(), key=lambda i:i[1], reverse=True):
    for _ in range(v):
        print(k, end=' ')
import sys
from bisect import bisect_left
n = int(sys.stdin.readline().strip())
coordinate = list(map(int, sys.stdin.readline().split()))
compressed = sorted(set(coordinate))
answer = [-1 for _ in range(n)]
for i, x in enumerate(coordinate):
    answer[i] = bisect_left(compressed, x)
print(*answer)
import sys
from collections import deque
from itertools import combinations

while True:
    input = deque(map(int, sys.stdin.readline().split()))
    k = input.popleft()
    if k == 0:
        break
    for next in combinations(input, 6):
       print(*next)
    print()
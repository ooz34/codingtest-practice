import sys
from collections import deque
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
arr = sorted(list(sys.stdin.readline().split()))

for next in combinations(arr, L):
    v_cnt = 0
    c_cnt = 0
    for ch in next:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            v_cnt += 1
        else:
            c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2:
            print(''.join(next))
            break
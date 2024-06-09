import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = int(sys.stdin.readline().rstrip())
opers = [sys.stdin.readline().rstrip() for _ in range(q)]

for op in opers:
    if op == '2':
        rvsd = arr[::-1]
        arr = list(zip(*rvsd))
    else:
        o, i = map(int, op.split())
        temp = deque(arr[i-1])
        temp.rotate(1)
        arr[i-1] = list(temp)

for row in arr:
    print(*row)
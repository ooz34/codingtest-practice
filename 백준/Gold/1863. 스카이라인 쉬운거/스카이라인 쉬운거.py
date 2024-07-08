import sys
n = int(sys.stdin.readline().rstrip())
heights = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    heights.append(y)
heights.append(0)

cnt = 0
stk = [0]
for y in heights:
    cur = y
    while stk[-1] > y:
        if stk[-1] != cur:
            cnt += 1
            cur = stk[-1]
        stk.pop()
    stk.append(y)

print(cnt)
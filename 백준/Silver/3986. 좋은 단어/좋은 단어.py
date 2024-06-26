import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    stk = []
    for ch in s:
        if stk and ch == stk[-1]:
            stk.pop()
        else:
            stk.append(ch)
    if not stk:
        cnt += 1
print(cnt)
import sys
n, m = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
heights.sort()

st, ed = 0, heights[-1]
while st <= ed:
    mid = (st + ed)//2
    tree = sum(h - mid for h in heights if h > mid)
    if tree >= m:
        st = mid + 1
    else:
        ed = mid - 1
print(ed)

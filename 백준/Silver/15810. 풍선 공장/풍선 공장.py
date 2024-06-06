import sys
n, m = map(int, sys.stdin.readline().split())
minutes = list(map(int, sys.stdin.readline().split()))

st, ed = 1, max(minutes)*m
while st < ed:
    mid = (ed + st)//2
    made = sum(mid//a for a in minutes)
    if made >= m:
        ed = mid
    else:
        st = mid + 1
print(ed)
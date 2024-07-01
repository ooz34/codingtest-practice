import sys
n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline().rstrip())
st = 1
ed = m
d = 0
for _ in range(j):
    app = int(sys.stdin.readline().rstrip())
    if app > ed:
        temp = app-ed
        d += temp
        st += temp
        ed = app
    elif app < st:
        temp = st-app
        d += temp
        ed -= temp
        st = app
print(d)
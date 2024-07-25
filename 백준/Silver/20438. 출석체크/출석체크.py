import sys
n, k, q, m = map(int, sys.stdin.readline().split())
students = [0]*(n+3)
klist = list(map(int, sys.stdin.readline().split()))
qlist = list(map(int, sys.stdin.readline().split()))
for q in qlist:
    if q in klist:
        continue
    else:
        for i in range(q, n+3, q):
            if i not in klist:
                students[i] = 1
ps = [0]*(n+3)
for i in range(3, n+3):
    if not students[i]:
        ps[i] = ps[i-1]+1
    else:
        ps[i] = ps[i-1]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(ps[e]-ps[s-1])
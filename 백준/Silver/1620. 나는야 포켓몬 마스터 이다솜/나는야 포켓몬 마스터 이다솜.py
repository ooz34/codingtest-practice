import sys
n, m = map(int, sys.stdin.readline().split())
idx_name = {}
name_idx = {}
for i in range(n):
    name = sys.stdin.readline().rstrip()
    idx_name[i+1] = name
    name_idx[name] = i+1
for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        print(idx_name[int(q)])
    else:
        print(name_idx[q])
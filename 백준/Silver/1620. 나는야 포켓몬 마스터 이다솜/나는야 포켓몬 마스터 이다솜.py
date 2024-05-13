import sys
n, m = map(int, sys.stdin.readline().split())
names = {}
idxs = {}
for i in range(1, n+1):
    temp = sys.stdin.readline().strip()
    names[temp] = i
    idxs[i] = temp
    
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(idxs[int(q)])
    else:
        print(names.get(q))
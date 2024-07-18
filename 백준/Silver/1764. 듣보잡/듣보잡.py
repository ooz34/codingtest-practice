import sys
n, m = map(int, sys.stdin.readline().split())
d = set()
for _ in range(n):
    d.add(sys.stdin.readline().rstrip())
b = set()
for _ in range(m):
    b.add(sys.stdin.readline().rstrip())
db = sorted(d & b)
print(len(db))
print(*db, sep='\n')
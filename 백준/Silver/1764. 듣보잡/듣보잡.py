import sys
n, m = map(int, sys.stdin.readline().split())
d_set = set()
b_set = set()
for i in range(n):
    d_set.add(sys.stdin.readline().strip())
for i in range(m):
    b_set.add(sys.stdin.readline().strip())
it = sorted(d_set & b_set)
print(len(it))
print(*it, sep='\n')
import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
tree = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
q = int(sys.stdin.readline().rstrip())
for _ in range(q):
    t, k = map(int, sys.stdin.readline().split())
    if t==1:
        if len(tree[k]) < 2:
            print('no')
        else:
            print('yes')
    else:
        print('yes')
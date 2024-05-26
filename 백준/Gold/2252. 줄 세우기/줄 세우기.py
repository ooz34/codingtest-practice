import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
indgr = [0] *(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indgr[b] += 1

ans = []
q = deque()
for i in range(1, n+1):
    if not indgr[i]:
        q.append(i)
while q:
    x = q.popleft()
    ans.append(x)
    for node in graph[x]:
        indgr[node] -= 1
        if not indgr[node]:
            q.append(node)
            
print(*ans)
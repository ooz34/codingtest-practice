import sys
from collections import deque
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)    

cnt = 0
q = deque()
q.append([1, 0])
visited[1] = True
while q:
    x, depth = q.popleft()
    if depth > 1:
        continue
    for i in graph[x]:
        if not visited[i]:
            q.append([i, depth + 1])
            visited[i] = True
            cnt += 1
print(cnt)
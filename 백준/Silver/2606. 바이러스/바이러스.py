import sys
from collections import deque
n = int(sys.stdin.readline().strip())
e = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)    

cnt = 0
q = deque([1])
visited[1] = True
while q:
    x = q.popleft()
    for i in graph[x]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            cnt += 1
print(cnt)
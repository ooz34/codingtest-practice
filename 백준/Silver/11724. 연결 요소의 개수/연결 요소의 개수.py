import sys
from collections import deque

def bfs(node):
	queue = deque()
	visited[node] = 1
	queue.append(node)
	while queue:
		x = queue.popleft()
		for i in graph[x]:
			if not visited[i]:
				queue.append(i)
				visited[i] = visited[x] + 1
				
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(n+1)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        answer += 1
print(answer)
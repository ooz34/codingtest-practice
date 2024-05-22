import sys
from collections import deque

def bfs(node):
	queue = deque()
	queue.append(node)
	while queue:
		x = queue.popleft()
		for i in graph[x]:
			if not p_node[i]:
				queue.append(i)
				p_node[i] = x
	
n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
p_node = [False]*(n+1)
bfs(1)
for i in range(2, n+1):
    print(p_node[i])
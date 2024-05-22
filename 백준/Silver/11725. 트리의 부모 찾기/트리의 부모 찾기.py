import sys
sys.setrecursionlimit(10**6)

def dfs(node):
	for i in graph[node]:
	    if not p_node[i]:
	        p_node[i] = node
	        dfs(i)
    
n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
p_node = [False]*(n+1)
dfs(1)
for i in range(2, n+1):
    print(p_node[i])
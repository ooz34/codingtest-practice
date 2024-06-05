import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [[-1, 0] for _ in range(100001)]

queue = deque([n])
visited[n] = [0, 1]

while queue:
    x = queue.popleft()
    
    for i in [x+1, x-1, 2*x]:
        if 0 <= i < 100001:
            if visited[i][0] == -1:
                queue.append(i)
                visited[i][0] = visited[x][0] + 1
                visited[i][1] = visited[x][1]
            elif visited[i][0] == visited[x][0] + 1:
                visited[i][1] += visited[x][1]

print(*visited[k], sep='\n')
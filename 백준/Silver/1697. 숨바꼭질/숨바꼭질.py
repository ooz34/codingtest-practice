import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [-1 for _ in range(100001)]

queue = deque([N])
visited[N] = 0

while queue:
    x = queue.popleft()
    if x == K:
        print(visited[x])
    for i in [x+1, x-1, 2*x]:
        if 0<= i < 100001 and visited[i] == -1:
            queue.append(i)
            visited[i] = visited[x] + 1
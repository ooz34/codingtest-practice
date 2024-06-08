import sys, heapq
from collections import deque

n, k = map(int, sys.stdin.readline().split())
INF = int(1e9)
d = [INF]*100001

queue = []
heapq.heappush(queue, (0, n))
d[n] = 0
while queue:
    dist, now = heapq.heappop(queue)
    if d[now] < dist:
        continue
    for i in [now+1, now-1, 2*now]:
        if 0<= i <= 100000:
            if i == 2*now and dist <d[i]:
                d[i] = dist
                heapq.heappush(queue, (dist, i))
            elif i != 2*now and dist+1 < d[i]:
                d[i] = dist + 1
                heapq.heappush(queue, (dist+1, i))
print(d[k])
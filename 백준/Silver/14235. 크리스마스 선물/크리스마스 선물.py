import sys, heapq
n = int(sys.stdin.readline().rstrip())
hq = []
for _ in range(n):
    q = sys.stdin.readline().rstrip()
    if q == '0':
        if not hq:
            print(-1)
        else:
            print(-heapq.heappop(hq))
    else:
        gifts = list(map(int, q.split()))
        for i in range(1, gifts[0]+1):
            heapq.heappush(hq, -gifts[i])
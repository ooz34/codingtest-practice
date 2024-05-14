import sys, heapq
n = int(sys.stdin.readline().strip())
hq = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if not x:
        print(heapq.heappop(hq)[1] if hq else 0)
    else:
        heapq.heappush(hq, (abs(x), x))
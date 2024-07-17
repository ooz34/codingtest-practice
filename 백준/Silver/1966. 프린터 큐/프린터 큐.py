import sys, heapq
def printer(plist, m):
    h = []
    ans = 1
    for p in plist:
        heapq.heappush(h, -p)
    while h:
        for i, p in enumerate(plist):
            if p == -h[0]:
                if i == m:
                    return ans
                heapq.heappop(h)
                ans += 1

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    plist = list(map(int, sys.stdin.readline().split()))
    print(printer(plist, m))
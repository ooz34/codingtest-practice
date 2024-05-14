import sys, heapq
n = int(sys.stdin.readline().strip())
hq = []
for _ in range(n):
    heapq.heappush(hq, int(sys.stdin.readline().strip()))
answer = 0
while len(hq) > 1:
    min1 = heapq.heappop(hq)
    min2 = heapq.heappop(hq)
    answer += min1 + min2
    heapq.heappush(hq, min1 + min2)
print(answer)
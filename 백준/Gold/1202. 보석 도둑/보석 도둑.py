import sys, heapq
n, k = map(int, sys.stdin.readline().split())
jewels = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
jewels.sort()
bags = [int(sys.stdin.readline().strip()) for _ in range(k)]
bags.sort()

answer = 0
max_val = []
for bag in bags:
    while jewels:
        if jewels[0][0] <= bag:
            heapq.heappush(max_val, (-jewels[0][1], jewels[0][0]))
            heapq.heappop(jewels)
        else:
            break
    if max_val:
        answer += -heapq.heappop(max_val)[0]
print(answer)
import sys, heapq
t = int(sys.stdin.readline().strip())

for _ in range(t):
    k = int(sys.stdin.readline().strip())
    minq = []
    maxq = []
    cnt = {}
    for _ in range(k):
        ch, n = sys.stdin.readline().split()
        x = int(n)
        if ch == 'I':
            heapq.heappush(minq, x)
            heapq.heappush(maxq, -x)
            if x in cnt:
                cnt[x] += 1
            else:
                cnt[x] = 1
        else:
            if x == 1:
                while maxq:
                    num = -heapq.heappop(maxq)
                    if cnt[num] > 0:
                        cnt[num] -= 1
                        break
            else:
                while minq:
                    num = heapq.heappop(minq)
                    if cnt[num] > 0:
                        cnt[num] -= 1
                        break
                    
    while minq and cnt[minq[0]] == 0:
        heapq.heappop(minq)
    while maxq and cnt[-maxq[0]] == 0:
        heapq.heappop(maxq)
        
    if not minq or not maxq:
        print('EMPTY')
    else:
        print(-maxq[0], minq[0])
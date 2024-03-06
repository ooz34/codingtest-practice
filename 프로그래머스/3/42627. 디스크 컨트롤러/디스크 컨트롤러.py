import heapq

def solution(jobs):
    heap = []  # 작업 소요 기간 기준 최소 힙
    cnt = len(jobs)
    now = 0
    sum = 0
    heapq.heapify(jobs)
    
    while jobs or heap:
        
        # 대기 큐 삽입
        while jobs and jobs[0][0] <= now:
            temp = heapq.heappop(jobs)
            heapq.heappush(heap, (temp[1], temp[0]))
        
        # 대기 큐 없을 때
        if len(heap)==0:
            now += 1
        # 대기 큐 있을 때
        else:
            temp = heapq.heappop(heap)
            now += temp[0]
            sum += now - temp[1]
    
    return sum//cnt
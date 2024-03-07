import heapq

def solution(operations):
    heap = []
    max_heap = []
    
    for i in operations:
        d, num = i.split()
        
        #삽입
        if d =='I':
            heapq.heappush(heap, int(num))
            heapq.heappush(max_heap, (int(num)*-1, int(num)))
        # 빈 큐 처리
        elif len(heap)==0:
            pass
        # 최댓값 삭제
        elif num =='1':
            max_val = heapq.heappop(max_heap)
            heap.remove(max_val[1])
            heapq.heapify(heap)
        # 최솟값 삭제            
        elif num == '-1':
            min_val = heapq.heappop(heap)
            max_heap.remove((min_val*-1, min_val))
            heapq.heapify(max_heap)
            
    return [0, 0] if not heap else [max_heap[0][1], heap[0]]
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K:
        
        # 스코빌지수를 K이상으로 만들 수 없는 경우 처리
        if len(scoville)==1:
            return -1
        
        mixed = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, mixed)
        
        answer += 1
    
    return answer
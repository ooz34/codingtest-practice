
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    otb = deque()
    
    while truck_weights or otb:
        
        answer += 1
        
        if otb and answer - otb[0][1] >= bridge_length:
            weight += otb[0][0]
            otb.popleft()
            
        if truck_weights and weight >= truck_weights[0]:
            weight -= truck_weights[0]
            otb.append((truck_weights[0], answer))
            truck_weights.pop(0)         
    
    return answer
from collections import Counter

def solution(clothes):
    answer = 1
    count = Counter([kind for name, kind in clothes])
    
    for v in count.values():
        answer *= v+1
    
    return answer -1
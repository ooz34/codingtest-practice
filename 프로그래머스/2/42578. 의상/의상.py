def solution(clothes):
    answer = 1
    count = {}
    
    for val, kind in clothes:
        if kind not in count:
            count[kind] = 1
        else:
            count[kind] += 1
         
    for k,v in count.items():
        answer *= v+1
    
    return answer - 1
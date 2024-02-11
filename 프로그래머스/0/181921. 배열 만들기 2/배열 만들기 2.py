def solution(l, r):
    answer = []
    
    for n in range(l, r + 1):
        for c in str(n):
            if c not in ['0','5']:
                break
        else:
            answer.append(n)
            
    if not answer:
        return [-1]
    
    return answer
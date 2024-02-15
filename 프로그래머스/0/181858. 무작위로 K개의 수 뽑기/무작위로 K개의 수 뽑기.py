def solution(arr, k):
    answer = []
    
    for n in arr:
        if len(answer) ==k:
            break
        if n in answer:
            continue
        answer.append(n)
        
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    
    return answer

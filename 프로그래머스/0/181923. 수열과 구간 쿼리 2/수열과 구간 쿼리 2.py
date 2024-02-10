def solution(arr, queries):    
    answer = []
    
    for s, e, k in queries:
        flag = False
        for i in sorted(arr[s:e+1]):
            if i > k:
                answer.append(i)
                flag = True
                break
            
        if not flag:
            answer.append(-1)
             
    return answer
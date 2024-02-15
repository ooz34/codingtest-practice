def solution(arr, flag):
    answer = []
    
    for n, f in zip(arr, flag):
        if f:
            for j in range(2*n):
                answer.append(n)   
        else:
            for j in range(n):
                answer.pop()
    
    return answer
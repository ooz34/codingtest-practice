def solution(n):
    answer = [[0 for x in range(n)] for y in range(n)]
    
    for i, arr in enumerate(answer):
        for j in range(n):
            if i == j:
                arr[j] += 1      
      
    return answer
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p) + 1):
        for n, j in enumerate(p):
            if t[i+n] < j:
                answer += 1
                break
            elif t[i+n] > j:
                break
        else:
            answer += 1    
    return answer
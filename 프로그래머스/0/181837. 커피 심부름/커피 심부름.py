def solution(order):
    answer = 0
    for e in order:
        if "latte" in e:
            answer += 5000
            continue
        answer += 4500
    
    return answer
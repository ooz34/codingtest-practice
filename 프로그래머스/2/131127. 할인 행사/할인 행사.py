def solution(want, number, discount):
    answer = 0
    wants = dict(zip(want, number))

    for i in range(len(discount)-9):
        target = discount[i:i+10]
        
        for name, cnt in wants.items():
            if target.count(name) < cnt:
                break
        else:
            answer += 1
        
    return answer
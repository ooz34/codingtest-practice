def solution(numLog):
    answer = ''
    control_dict = {1:'w', -1:'s', 10:'d', -10:'a'}
    control = [numLog[i+1] - numLog[i] for i in range(len(numLog)-1)]

    for key in control:
        answer += control_dict.get(key)
    
    return answer
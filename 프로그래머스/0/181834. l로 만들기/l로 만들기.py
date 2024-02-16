def solution(myString):
    answer = ''
    for ch in myString:
        if ch < 'l':
            answer += 'l'
            continue
        answer += ch
    
    return answer
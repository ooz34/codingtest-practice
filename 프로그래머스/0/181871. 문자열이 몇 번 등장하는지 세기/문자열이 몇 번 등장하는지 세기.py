def solution(myString, pat):
    answer = 0
    start = 0

    while True:
        idx = myString.find(pat, start)

        if idx == -1:
            break
        
        answer += 1
        start = idx + 1
    
    return answer
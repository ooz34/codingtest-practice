from collections import Counter

def solution(s):
    answer = [0, 0]
    
    while s != '1':
        cnt = Counter(s)
        answer[1] += cnt['0']
        s = format(cnt['1'], 'b')
        answer[0] += 1
    
    return answer

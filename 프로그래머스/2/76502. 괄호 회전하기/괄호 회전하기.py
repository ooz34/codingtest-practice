from collections import deque

def solution(s):
    answer = 0
    q = deque(s)    
    
    for _ in range(len(s)):
        curr = []
        for b in q:
            curr.append(b)
            if curr[-2:] in [['[',']'], ['(',')'], ['{','}']]:
                del curr[-2:]
        else:
            if not curr:
                answer += 1
            
        temp = q.popleft()
        q.append(temp)
    
    return answer
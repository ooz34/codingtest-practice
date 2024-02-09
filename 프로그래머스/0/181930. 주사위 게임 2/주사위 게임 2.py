def solution(a, b, c):
    value = [a, b, c]
    count = set(value)
    answer = 1
    
    for i in range(3, len(count)-1, -1):
         answer *= sum([val**(-i+4) for val in value])

    return answer
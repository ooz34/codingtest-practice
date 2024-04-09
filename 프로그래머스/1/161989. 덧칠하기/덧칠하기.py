def solution(n, m, section):
    answer = 0
    painted = 0
    for i in section:
        if painted < i:
            answer += 1
            painted = i + m -1
    return answer
def solution(n):
    answer = 0
    a1 = 0
    a2 = 1

    for _ in range(n):
      a1, a2 = a2, a1+a2
      answer = a2 % 1234567

    return answer
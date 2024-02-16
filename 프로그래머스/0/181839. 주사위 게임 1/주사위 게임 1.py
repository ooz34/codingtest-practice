def solution(a, b):
    if a % 2 == 1:
        if b % 2 == 1:
            return a**2 + b**2
        return 2 * (a + b)
    if b % 2 == 1:
        return 2 * (a + b)
    return abs(a - b)
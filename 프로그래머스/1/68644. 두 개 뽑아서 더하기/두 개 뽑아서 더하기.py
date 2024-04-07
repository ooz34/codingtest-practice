from itertools import combinations

def solution(numbers):
    nC2 = list(combinations(numbers, 2))
    return sorted(set([x + y for x, y in nC2]))
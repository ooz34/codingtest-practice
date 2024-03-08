from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)
    nPr = set(int(''.join(p)) for i in range(1, len(nums) + 1) for p in permutations(nums, i))
    answer = sum(1 for n in nPr if is_prime(n))

    return answer
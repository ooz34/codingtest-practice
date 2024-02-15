def solution(arr):
    n = 0
    
    while len(arr) > 2**n:
        n += 1

    arr += [0] * (2**n - len(arr))
    
    return arr
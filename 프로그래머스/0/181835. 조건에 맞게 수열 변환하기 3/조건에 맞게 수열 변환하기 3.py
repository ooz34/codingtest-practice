def solution(arr, k):
    if k % 2:
        return [x * k for x in arr]   
    return [x + k for x in arr]

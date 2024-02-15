def solution(arr):
    for i, n in enumerate(arr):
        if n >= 50:
            if n % 2 == 0:
                arr[i] = n // 2
        else:
            if n % 2 == 1:
                arr[i] = n * 2
    return arr
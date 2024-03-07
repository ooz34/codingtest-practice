def solution(A, K):
    if not A: return A

    length = len(A)

    for shift in range(K % length):
        temp = A[-1]
        for i in range(length-1, 0, -1):
            A[i] = A[i-1]
        A[0] = temp

    return A
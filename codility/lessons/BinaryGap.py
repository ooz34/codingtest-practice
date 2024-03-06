def solution(N):

    binaryNum = bin(N)[2:]

    n1 = 0
    longest = 0

    for i, b in enumerate(binaryNum):
        if b == '1':
            gap = i - n1 -1
            if longest < gap:
                longest = gap
            n1 = i

    return longest
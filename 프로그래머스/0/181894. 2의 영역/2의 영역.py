def solution(arr):
    ridx = 1
    for i,n in reversed(list(enumerate(arr))):
        if n == 2:
            ridx += i
            break
    else:
        return [-1]
    
    return arr[arr.index(2):ridx]
def solution(arr):
    len_fst = len(arr)
    len_scnd = len(arr[0])
    
    if len_fst > len_scnd:
        arr = [row + [0] * (len_fst - len_scnd) for row in arr]
    elif len_fst < len_scnd:
        arr += [[0] * len_scnd] * (len_scnd - len_fst)
    
    return arr
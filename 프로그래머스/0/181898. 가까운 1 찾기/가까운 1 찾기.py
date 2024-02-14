def solution(arr, idx):
    for i,e in enumerate(arr[idx:]):
        if e == 1:
            return idx+i
    
    return -1
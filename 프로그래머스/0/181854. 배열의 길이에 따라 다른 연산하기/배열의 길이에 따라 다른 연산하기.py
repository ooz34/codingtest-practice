def solution(arr, n):
    start = 0
    
    if len(arr) % 2 == 0:
        start += 1
    
    for i in range(start,len(arr),2):
        arr[i] += n
    
    return arr
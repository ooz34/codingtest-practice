def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
            continue
        if stk[-1] == arr[i]:
            stk.pop()
            i += 1
            continue
        stk.append(arr[i])
        i += 1
    
    return stk if stk else [-1]
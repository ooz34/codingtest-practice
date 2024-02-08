def solution(code):
    mode = bool(0)
    ret = ''
    
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = not mode
            continue
        
        if mode==0:
            if idx%2==0:
                ret += code[idx]
                continue
            continue
        
        if idx%2==1:
            ret += code[idx]
    
    if not ret:
        ret = "EMPTY"
    
    return ret
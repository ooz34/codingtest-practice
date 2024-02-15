def solution(myString):
    str_list = list(myString)
    
    for i, c in enumerate(str_list):
        if c.lower() == 'a':
            str_list[i] = c.upper()
            continue
        str_list[i] = c.lower()
        
    return ''.join(str_list)
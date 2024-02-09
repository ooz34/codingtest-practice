def solution(num_list):

    list_odd = list(filter(lambda x: x % 2 == 1, num_list))
    list_even = list(filter(lambda x: x % 2 == 0, num_list))
    
    str_odd = ''.join(list(map(str,list_odd)))
    str_even = ''.join(list(map(str,list_even)))
    
    return int(str_odd) + int(str_even)
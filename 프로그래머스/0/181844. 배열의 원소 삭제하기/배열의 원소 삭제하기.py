def solution(arr, delete_list):
    answer = []
    
    for n in arr:
        if n in delete_list:
            continue
        answer.append(n)
    
    return answer
def solution(todo_list, finished):
    answer = []
    
    for i, f in enumerate(finished):
        if not f:
            answer.append(todo_list[i])
    
    return answer
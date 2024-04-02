def solution(ingredient):
    answer = 0
    curr = []
    
    for ing in ingredient:
        curr.append(ing)
        if curr[-4:] == [1, 2, 3, 1]:
            answer += 1
            curr.pop()
            curr.pop()
            curr.pop()
            curr.pop()
            
    return answer
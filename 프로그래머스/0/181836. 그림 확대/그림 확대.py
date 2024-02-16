def solution(picture, k):
    answer = []
    
    for pic in picture:
        new_pic = ''
        for c in pic:
            new_pic += c * k
        answer += [new_pic] * k
    
    return answer
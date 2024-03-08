def solution(answers):
    supoja = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    count = {1:0, 2:0, 3:0}
    
    for qnum, answer in enumerate(answers):
        for key, val in supoja.items():
            if answer == val[qnum % len(val)]:
                count[key] += 1
    
    return [k for k,v in count.items() if v == max(count.values())]
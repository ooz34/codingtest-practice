def solution(survey, choices):  
    tot_point = {'R':0, 'T':0, 'C': 0, 'F' : 0, 'J': 0, 'M' : 0, 'A': 0, 'N' : 0}
    point =[0, 3, 2, 1, 0, 1, 2, 3]
    answer = ['R', 'C', 'J', 'A']
    
    for q, p in zip(survey, choices):
        if p < 4:
            tot_point[q[0]] += point[p]
        elif p == 4:
            continue    
        else:
            tot_point[q[1]] += point[p]     
    
    if tot_point['R'] < tot_point['T']:
        answer[0] = 'T'
    if tot_point['C'] < tot_point['F']:
        answer[1] = 'F'    
    if tot_point['J'] < tot_point['M']:
        answer[2] = 'M'    
    if tot_point['A'] < tot_point['N']:
        answer[3] = 'N'
    
    return ''.join(answer)
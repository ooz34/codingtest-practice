def solution(priorities, location):
    value = priorities[location]
    
    smaller_count = sum(1 for val in priorities[:location] if val < value)

    priorities = list(filter(lambda x: x>=value, priorities))
        
    s_prior = sorted(priorities,reverse=True)
    location -= smaller_count
    
    if(s_prior.count(value)==1):
        return s_prior.index(value)+1
    
    priorities[location] = str(value)
            
    for i in range(s_prior.index(value)):
        priorities = priorities[priorities.index(s_prior[i])+1:] + priorities[:priorities.index(s_prior[i])]
    
    return s_prior.index(value) + priorities.index(str(value)) + 1
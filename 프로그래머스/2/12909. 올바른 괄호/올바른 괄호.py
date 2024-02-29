def solution(s):
    lists = list(s)
    cnt=0;
    
    if lists[0]==")" or len(lists)%2==1:
        return False
    elif lists.count(")") != len(lists)/2:
        return False
    
    for i in lists:
        if i=="(": cnt+=1
        else:      cnt-=1
        
        if cnt<0:
            return False
    
    return True
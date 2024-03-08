def solution(sizes):
    maxW, maxH=0, 0;
    
    for i in sizes:
        if(maxW<max(i)):
            maxW=max(i)
        if(maxH<min(i)):
            maxH=min(i)
    
    return maxW*maxH
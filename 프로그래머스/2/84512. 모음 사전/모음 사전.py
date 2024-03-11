import itertools

def solution(word):
    source = ("A","E","I","O","U")
    diction=[]
    
    for i in range(1, len(source)+1):
        for j in itertools.product(source, repeat=i):
            diction.append(''.join(j))
    
    return sorted(diction).index(word)+1
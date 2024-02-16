def solution(rank, attendance):
    rnk_i = []
    
    for i, (r, f) in enumerate(zip(rank, attendance)):
        if f:
            rnk_i.append([r, i])
            
    rnk_i.sort()
    
    return  10000 * rnk_i[0][1] + 100 * rnk_i[1][1] + rnk_i[2][1]
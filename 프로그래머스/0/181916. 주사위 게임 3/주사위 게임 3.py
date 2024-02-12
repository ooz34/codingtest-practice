from collections import Counter

def solution(a, b, c, d):
    count = Counter([a,b,c,d]).most_common()

    if len(count) == 1:
        return 1111 * a
    
    if len(count) == 4:
        return min(a,b,c,d)
    
    if len(count) == 3:
        return count[1][0] * count[2][0]
     
    if count[0][1] == 2:
        return (count[0][0]+count[1][0]) * abs(count[0][0]-count[1][0])
    
    return (10 * count[0][0] + count[1][0])**2
from collections import Counter

def solution(n, control):
    counter = Counter(control)
    
    return n + counter.get('w') - counter.get('s') + 10*(counter.get('d')-counter.get('a'))
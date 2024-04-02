from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    alph = [ch for ch in ascii_lowercase if ch not in skip]
    len_alph = len(alph)
    
    for ch in s:
        answer += alph[(alph.index(ch)+index) % len_alph]
    
    return answer
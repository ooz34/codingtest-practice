from collections import Counter

def solution(strArr):
    counter = Counter([len(s) for s in strArr]).most_common() 
    return counter[0][1]
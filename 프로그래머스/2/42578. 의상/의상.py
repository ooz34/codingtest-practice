from collections import Counter
from functools import reduce

def solution(clothes):
    count = Counter([kind for name, kind in clothes])
    return reduce(lambda x, y: x*(y+1), count.values(), 1) - 1
from collections import Counter

def solution(k, tangerine):
    cnt = Counter(tangerine).most_common()
    kinds = 0
    packed = 0

    for _, count in cnt:
        packed += count
        kinds += 1
        if packed >= k:
            break    

    return kinds
from collections import Counter

def solution(A):
    counts = Counter(A).most_common()

    for n, cnt in reversed(counts):
        if cnt % 2 == 1:
            return n

# O(N) or O(N*log(N))
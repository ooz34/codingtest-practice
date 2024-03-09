import itertools

def solution(k, dungeons):
    max_cnt = 0

    for perm in itertools.permutations(dungeons, len(dungeons)):
        cur_k = k
        cnt = 0
        for min_k, ddc_k in perm:
            if min_k <= cur_k:
                cur_k -= ddc_k
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt
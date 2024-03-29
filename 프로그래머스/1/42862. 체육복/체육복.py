def solution(n, lost, reserve):
    real_lost = [l for l in lost if l not in reserve]
    real_rsv = [r for r in reserve if r not in lost]
    answer = n - len(real_lost)
    rsv_dict = {r:1 for r in real_rsv}
    
    for num in sorted(real_lost):
        for r in [num-1, num+1]:
            if r in rsv_dict:
                if rsv_dict[r]:
                    rsv_dict[r] = 0
                    answer += 1
                    break
    return answer
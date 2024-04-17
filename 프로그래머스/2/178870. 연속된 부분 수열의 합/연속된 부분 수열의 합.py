def solution(sequence, k):
    seq_len = len(sequence)
    prefix_sum = [0 for _ in range(seq_len + 1)]
    min_len = float('inf')
    start_idx = 0
    
    for i in range(1, seq_len +1):
        prefix_sum[i] = prefix_sum[i-1] + sequence[i-1]
        
    start = 0
    end = 0    
    while start < seq_len:
        curr_sum = prefix_sum[end] - prefix_sum[start]
        
        if curr_sum < k:
            end += 1
            if end == seq_len + 1:
                break
        else:
            if curr_sum == k and end - start < min_len:
                min_len = end -start
                start_idx = start
            start += 1                
    
    return [start_idx, start_idx + min_len - 1]
import sys
n, s = map(int, sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
cnt = 0

def backtrack(idx, seq_sum):
    global cnt
    if idx == n:
        if seq_sum == s:
            cnt += 1
        return
    
    backtrack(idx + 1, seq_sum + seq[idx])
    backtrack(idx + 1, seq_sum)
        
backtrack(0, 0)
if s==0: cnt -= 1
print(cnt)
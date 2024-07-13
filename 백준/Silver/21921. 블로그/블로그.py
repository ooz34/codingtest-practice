import sys
n, x = map(int, sys.stdin.readline().split())
vpd = list(map(int, sys.stdin.readline().split()))

p_sum = sum(vpd[:x])
max_v = p_sum
p_cnt = 1
for i in range(x, n):
    p_sum -= vpd[i-x]
    p_sum += vpd[i]
    if p_sum == max_v:
        p_cnt += 1
    elif p_sum > max_v:
        max_v = p_sum
        p_cnt = 1

if not max_v:
    print('SAD')
else:
    print(max_v)
    print(p_cnt)
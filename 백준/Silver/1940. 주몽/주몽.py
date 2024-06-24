import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
st, nd = 0, n-1
cnt = 0
while st < nd:
    temp = nums[st] + nums[nd]
    if temp < m:
        st += 1
    elif temp > m:
        nd -= 1
    else:
        cnt += 1
        nd -= 1
print(cnt)
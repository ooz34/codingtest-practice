import sys
n = int(sys.stdin.readline().strip())
cnt = {}
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1
for i in range(1, 10001):
    if i in cnt:
        for _ in range(cnt[i]):
            print(i)
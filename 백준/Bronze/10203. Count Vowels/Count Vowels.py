import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    cnt = 0
    for ch in s:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    print('The number of vowels in ', s, ' is ', cnt, '.', sep='')
import sys
a, b, c = map(int, sys.stdin.readline().split())
cnt = [0]*101
for _ in range(3):
    st, ed = map(int, sys.stdin.readline().split())
    for i in range(st+1, ed+1):
        cnt[i] += 1
fare = {0:0, 1:a, 2:b*2, 3:c*3}
tot = 0
for c in cnt:
    tot += fare[c]
print(tot)
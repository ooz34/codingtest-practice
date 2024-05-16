import sys
tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    n = int(sys.stdin.readline().strip())
    counter = {}
    answer = 1
    for _ in range(n):
        item, kind = sys.stdin.readline().split()
        if kind not in counter:
            counter[kind] = 1
        else:
            counter[kind] += 1
    for cnt in counter.values():
        answer *= cnt + 1
    print(answer-1)
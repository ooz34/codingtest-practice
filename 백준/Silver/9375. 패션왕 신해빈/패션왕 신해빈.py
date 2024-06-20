import sys
tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    n = int(sys.stdin.readline().rstrip())
    kinds = {}
    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        if kind in kinds:
            kinds[kind] += 1
        else:
            kinds[kind] = 1
    ans = 1
    for v in kinds.values():
        ans *= v+1
    print(ans-1)
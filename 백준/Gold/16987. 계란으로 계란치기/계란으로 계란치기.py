import sys
n = int(sys.stdin.readline().rstrip())
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0
def sol(idx):
    global cnt
    if idx == n:
        cnt = max(cnt, sum(1 for egg in eggs if egg[0]<=0))
        return
    isBeaten = False
    if eggs[idx][0] > 0:
        for i in range(n):
            if eggs[i][0] > 0 and i != idx:
                isBeaten = True
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                sol(idx+1)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
        if not isBeaten:
            sol(idx+1)
    else:
        sol(idx+1)

sol(0)
print(cnt)
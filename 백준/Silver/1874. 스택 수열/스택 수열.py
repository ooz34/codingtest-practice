import sys
n = int(sys.stdin.readline().strip())
seq = [int(sys.stdin.readline().strip()) for _ in range(n)]
answer = []

stk = []
curr = 1
for num in seq:
    while curr <= num:
        stk.append(curr)
        answer.append('+')
        curr += 1
    if stk[-1] == num:
        stk.pop()
        answer.append('-')
    else:
        print('NO')
        break
else:
    print(*answer, sep='\n')
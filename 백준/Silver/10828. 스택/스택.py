import sys
n = int(sys.stdin.readline().strip())
opers = [sys.stdin.readline().strip() for _ in range(n)]

stk = []
for oper in opers:
    if oper == 'pop':
        if not stk:
            print(-1)
        else:
            print(stk.pop())
    elif oper == 'size':
        print(len(stk))
    elif oper == 'empty':
        if not stk:
            print(1)
        else:
            print(0)
    elif oper == 'top':
        if not stk:
            print(-1)
        else:
            print(stk[-1])
    else:
        o, n = oper.split()
        stk.append(int(n))
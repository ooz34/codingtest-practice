import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s=='.':
        break
    stk = []
    for ch in s:
        if ch in ['(', '[']:
            stk.append(ch)
        elif ch == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(ch)
                break
        elif ch == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(ch)
                break
    print('yes' if not stk else 'no')
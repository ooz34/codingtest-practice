import sys
s = sys.stdin.readline().rstrip()
e = list(sys.stdin.readline().rstrip())
len_e = len(e)

stk = []
for ch in s:
    stk.append(ch)
    if len(stk) >= len_e and stk[-len_e:] == e:
        del stk[-len_e:]
    
print(''.join(stk) if len(stk) else 'FRULA')
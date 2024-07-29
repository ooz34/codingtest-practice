import sys
while True:
    input = sys.stdin.readline().rstrip()
    if not input:
        break
    else:
        s, t = map(str, input.split())
        idx = 0
        isSubstr = False
        for ch in t:
            if ch == s[idx]:
                idx += 1
                if idx == len(s):
                    isSubstr = True
                    break
        if isSubstr:
            print('Yes')
        else:
            print('No')
import sys
from collections import Counter
cnt = Counter(sys.stdin.readline().strip().upper())
if len(cnt) == 1:
    print(cnt.most_common(1)[0][0])
else:
    a, b = cnt.most_common(2)
    if a[1] == b[1]:
        print('?')
    else:
        print(a[0])
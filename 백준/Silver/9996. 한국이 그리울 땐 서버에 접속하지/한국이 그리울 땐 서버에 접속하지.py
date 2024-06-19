import sys
n = int(sys.stdin.readline().rstrip())
st, ed = sys.stdin.readline().rstrip().split('*')
plen = len(st) + len(ed)
for _ in range(n):
    fname = sys.stdin.readline().rstrip()
    if len(fname) < plen:
        print('NE')
        continue
    if fname.startswith(st) and fname.endswith(ed):
        print('DA')
    else:
        print('NE')
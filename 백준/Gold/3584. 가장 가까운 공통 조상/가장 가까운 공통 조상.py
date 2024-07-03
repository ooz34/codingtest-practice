import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    plist = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        plist[b] = a
    ta, tb = map(int, sys.stdin.readline().split())
    ta_plist, tb_plist = [ta], [tb]
    while plist[ta]:
        ta_plist.append(plist[ta])
        ta = plist[ta]
    while plist[tb]:
        tb_plist.append(plist[tb])
        tb = plist[tb]
    ta_dep, tb_dep = len(ta_plist)-1, len(tb_plist)-1
    while ta_plist[ta_dep] == tb_plist[tb_dep]:
        ta_dep -= 1
        tb_dep -= 1
    print(ta_plist[ta_dep+1])
import sys
n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()
for num in mlist:
    st, ed = 0, n-1
    while st<=ed:
        mid = (st+ed)//2
        if nlist[mid] == num:
            print(1, end=' ')
            break
        elif num < nlist[mid]:
            ed = mid-1
        else:
            st = mid+1
    else:
        print(0, end=' ')
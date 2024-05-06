import sys

n = int(sys.stdin.readline().strip())
arr = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
target = list(map(int, sys.stdin.readline().split()))

for num in target:
    st = 0
    en = n-1
    found = False
    while st <= en:
        mid = (st+en)//2
        val = arr[mid]
        if val == num:
            print(1)
            found = True
            break
        elif val < num:
            st = mid + 1
        else:
            en = mid - 1
    if not found:
        print(0)
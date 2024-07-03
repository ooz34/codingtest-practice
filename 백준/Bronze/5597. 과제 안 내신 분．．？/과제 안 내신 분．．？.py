import sys
arr = [0 for _ in range(30)]
for _ in range(28):
    arr[int(sys.stdin.readline().rstrip())-1] = 1
for i, val in enumerate(arr):
    if not val:
        print(i+1)
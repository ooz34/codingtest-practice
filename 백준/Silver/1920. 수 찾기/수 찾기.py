import sys
from bisect import bisect_left

n = int(sys.stdin.readline().strip())
arr = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
target = list(map(int, sys.stdin.readline().split()))

for num in target:
	idx = bisect_left(arr, num)
	if idx < n and arr[idx] == num:
		print(1)
	else:
		print(0)
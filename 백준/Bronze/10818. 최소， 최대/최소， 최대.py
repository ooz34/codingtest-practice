import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
print(min(nums), max(nums))
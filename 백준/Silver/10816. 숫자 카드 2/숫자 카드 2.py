import sys
from collections import Counter
n = int(sys.stdin.readline().strip())
deck = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
counter = Counter(deck)
answer = [0 for _ in range(m)]

for i, num in enumerate(nums):
    nums[i] = counter[num]
print(*nums)
import sys
from collections import deque
nums = list(map(int, sys.stdin.readline().split()))

def clock_num(cards):
    dnum = deque(cards)
    rotations = []
    for _ in range(4):
        dnum.rotate(-1)
        rotations.append(int(''.join(map(str, dnum))))
    return min(rotations)

whole_num = set()
for i in range(1111, 10000):
    if '0' not in str(i):
        cards = list(map(int, str(i)))
        whole_num.add(clock_num(cards))

sorted_num = sorted(whole_num)
print(sorted_num.index(clock_num(nums))+1)
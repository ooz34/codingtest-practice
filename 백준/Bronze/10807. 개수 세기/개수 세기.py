import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
counter = Counter(sys.stdin.readline().split())
print(counter[sys.stdin.readline().rstrip()])
import sys
num = list(map(int, sys.stdin.readline().split()))
print(' '.join(map(str, sorted(num))))
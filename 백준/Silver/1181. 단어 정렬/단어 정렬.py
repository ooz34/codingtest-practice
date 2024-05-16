import sys
n = int(sys.stdin.readline().strip())
words = sorted(set(sys.stdin.readline().strip() for _ in range(n)))
words.sort(key=lambda x: len(x))
print(*words, sep='\n')
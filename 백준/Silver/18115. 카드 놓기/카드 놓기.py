import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

deck = deque([i for i in range(N,0,-1)])
answer = deque()

for a in reversed(A):
    if a == 1:
        answer.append(deck.pop())
        continue
    if a == 2:
        answer.insert(-1, deck.pop())
        continue
    answer.appendleft(deck.pop())
    
answer.reverse()        
print(" ".join(map(str, answer)))
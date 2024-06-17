import sys
shorts = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
shorts.sort()
exd = sum(shorts) - 100
for h in shorts:
    ano = exd-h
    if ano != h and ano in shorts:
        shorts.remove(h)
        shorts.remove(ano)
        break
print(*shorts, sep='\n')
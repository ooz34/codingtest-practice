import sys
mods = set()
for _ in range(10):
    mods.add(int(sys.stdin.readline().strip())%42)
print(len(mods))

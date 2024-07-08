import sys, re
pattern = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(int(sys.stdin.readline().rstrip())):
    if pattern.match(sys.stdin.readline().rstrip())==None:
        print('Good')
    else:
        print('Infected!')
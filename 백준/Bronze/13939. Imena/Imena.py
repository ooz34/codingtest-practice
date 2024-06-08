import sys, re
n = int(sys.stdin.readline().rstrip())
stns = re.split(r'[.!?]', sys.stdin.readline().strip())
for stn in stns:
    if stn.strip():
        names = re.findall(r'\b[A-Z][a-z]*\b', stn)
        print(len(names))
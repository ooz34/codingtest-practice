strks = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
ss = [strks[ord(ch)-65] for ch in input()]

if sum(ss)&1:
    print("I'm a winner!")
else:
    print("You're the winner?")
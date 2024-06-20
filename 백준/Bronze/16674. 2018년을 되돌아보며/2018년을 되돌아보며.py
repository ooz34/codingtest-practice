n = list(map(int, list(input().rstrip())))
counter = {2:0, 0:0, 1:0, 8:0}
for num in n:
    if num not in counter:
        print(0)
        exit(0)
    else:
        counter[num] += 1
        
vlist = counter.values()
if 0 in vlist:
    print(1)
elif len(set(vlist)) == 1:
    print(8)
else:
    print(2)
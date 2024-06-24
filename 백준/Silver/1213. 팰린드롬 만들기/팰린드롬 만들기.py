from collections import Counter
name = input()
len_name = len(name)
counter = Counter(name)
odd = 0
mid = []
for k, v in counter.items():
    if v&1:
        odd += 1
        mid.append(k)
sc = list(counter.items())
sc.sort()
if len_name&1:
    if odd == 1:
        temp = ''
        for ch, cnt in sc:
            temp += ch*(cnt//2)
        rev = list(temp)
        rev.reverse()
        res = temp + mid[0] + ''.join(rev)
        print(res)
    else:
        print("I'm Sorry Hansoo")    
elif not odd:
    temp = ''
    for ch, cnt in sc:
        temp += ch*(cnt//2)
    rev = list(temp)
    rev.reverse()
    res = temp + ''.join(rev)
    print(res)
else:
    print("I'm Sorry Hansoo")    
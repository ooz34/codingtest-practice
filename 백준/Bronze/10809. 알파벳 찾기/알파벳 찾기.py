import string
alist = {ch:i for i, ch in enumerate(list(string.ascii_lowercase))}
answer = [-1 for _ in range(len(alist))]
for i, ch in enumerate(input()):
    idx = alist[ch]
    if answer[idx] == -1:
        answer[idx] = i
print(*answer)
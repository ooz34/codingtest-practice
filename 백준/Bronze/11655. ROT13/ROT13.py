s = list(input())
for i, ch in enumerate(s):
    if 'A' <= ch <= 'Z':
        s[i] = chr(65 + ((ord(ch)+13)-65)%26)
    elif 'a' <= ch <= 'z':
        s[i] = chr(97 + ((ord(ch)+13)-97)%26)
print(''.join(s))
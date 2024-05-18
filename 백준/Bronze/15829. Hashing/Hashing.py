l = int(input())
string = input()
answer = 0
for i, ch in enumerate(string):
    answer += (ord(ch)-96)*pow(31,i)
print(answer % 1234567891)
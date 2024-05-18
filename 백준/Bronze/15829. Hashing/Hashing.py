l = int(input())
string = input()
answer = 0
for i, ch in enumerate(string):
    answer += (ord(ch)-96)*(31**i) % 1234567891
print(answer)
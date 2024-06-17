s = input()
rs = list(s)
rs.reverse()
print(1 if s == ''.join(rs) else 0)
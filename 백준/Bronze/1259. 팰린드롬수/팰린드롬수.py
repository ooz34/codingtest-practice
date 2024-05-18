while True:
    string = input()
    if string == '0':
        break
    r_str = list(string)
    r_str.reverse()
    if string == ''.join(r_str):
        print('yes')
    else:
        print('no')
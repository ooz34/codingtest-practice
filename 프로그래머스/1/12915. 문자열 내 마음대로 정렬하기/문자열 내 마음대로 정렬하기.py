def solution(strings, n):
    string_dict = sorted({s:s[n] for s in strings}.items(), key= lambda item: (item[1], item[0]))
    return [k for k, v in string_dict]
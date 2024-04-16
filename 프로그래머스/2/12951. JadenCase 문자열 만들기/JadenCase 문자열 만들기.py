def solution(s):
    words = s.split(' ')
    capitalized = [word.capitalize() for word in words]
    return ' '.join(capitalized)

import string

def solution(my_string):
    alpha = list(string.ascii_uppercase) + list(string.ascii_lowercase)
    counter = {char : 0 for char in alpha}
    
    for c in my_string:
        counter[c] += 1
        
    return list(counter.values())
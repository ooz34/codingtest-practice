
def solution(keymap, targets):
    answer = [0 for _ in range(len(targets))]
    keymap_set = set()
    targets_set = set()

    for keyarr in keymap:
        keymap_set.update(keyarr)
    for target in targets:
        targets_set.update(target)
    
    missing_key = targets_set - keymap_set
    key_press = {k:0 for k in targets_set}
    
    for key in targets_set:
        if key in  missing_key:
            key_press[key] = -1
            continue
        
        flag = True
        while flag:
            flag = False
            for i in range(100):
                for keyarr in keymap:
                    if len(keyarr) < i+1:
                        continue
                    if keyarr[i] in key_press and key_press[keyarr[i]] == 0:
                        key_press[keyarr[i]] = i+1
                        if all(v != 0 for v in key_press.values()):
                            flag = False    
                            break
                if flag:
                    break
        
    for i, target in enumerate(targets):
        for char in target:
            if key_press[char] == -1:
                answer[i] = -1
                break
            answer[i] += key_press[char]

    return answer
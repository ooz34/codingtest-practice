from collections import deque

def solution(bandage, health, attacks):
    castingTime, recovHPerSec, addRecovH = bandage
    attack = deque(attacks)
    hp = health
    recovTime = 0
    
    for sec in range(attacks[-1][0] + 1):
        nextAttck = attack[0]
        
        if sec == nextAttck[0]:
            hp -= nextAttck[1]
            attack.popleft()
            recovTime = 0
            if hp <= 0:
                return -1
            continue    

        hp += recovHPerSec
        recovTime += 1
        if recovTime == castingTime:
            hp += addRecovH
            recovTime = 0
        hp = min(health, hp)
   
    return hp
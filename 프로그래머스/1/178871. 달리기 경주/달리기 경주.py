def solution(players, callings):
    rank = {player:i for i, player in enumerate(players)}
    
    for name in callings:
        passed_idx = rank[name] - 1    
        rank[players[passed_idx]] += 1
        rank[name] -= 1
        players[passed_idx], players[passed_idx+1] =  players[passed_idx+1],  players[passed_idx]
    
    return players
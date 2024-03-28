def solution(wallpaper):
    min_x, min_y = 51, 51
    max_x, max_y = 0, 0
    
    for i, row in enumerate(wallpaper):
        if '#' in row:
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, row.index('#'))
            max_y = max(max_y, row.rindex('#'))  
            
    return [min_x, min_y, max_x+1, max_y+1]
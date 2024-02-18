def solution(data, ext, val_ext, sort_by):
    answer = []
    col_name = ['code', 'date', 'maximum', 'remain']
    ext_idx = col_name.index(ext)
    
    for row in data:
        if row[ext_idx] < val_ext:
            answer.append(row)
            
    answer.sort(key=lambda x:x[col_name.index(sort_by)])    
        
    return answer
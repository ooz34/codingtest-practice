def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split('.'))
    expiration_date = {}
    
    for term in terms:
        term_type, m = term.split(' ')
        dy = int(m)//12
        dm = int(m)%12
        
        if tm > dm:
            expiration_date[term_type] = [ty-dy, tm-dm, td]
        else:
            expiration_date[term_type] = [ty-dy-1, tm-dm + 12, td]
    
    for i, privacy in enumerate(privacies):
        pdate, term_type = privacy.split(' ')
        py, pm, pd = map(int, pdate.split('.'))
        ey, em, ed = expiration_date[term_type]
        
        if (py, pm, pd) > (ey, em, ed):
            continue
        answer.append(i+1)
    
    return answer
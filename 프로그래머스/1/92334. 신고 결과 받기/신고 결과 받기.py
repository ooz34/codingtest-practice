def solution(id_list, report, k):
    answer = {id:0 for id in id_list}
    report_list = {id:[] for id in id_list}
    report_set = set(report)
 
    for r in report_set:
        reporter, reportee = r.split(' ')
        report_list[reportee].append(reporter)
        
    for name, reporters in report_list.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[reporter] += 1
    
    return list(answer.values())
import re
import copy
def solution(n, t, m, timetable):
    res = []
    for i in timetable:
        a = re.compile('\d+').findall(i)
        res.append(list(map(int, a)))
    a = {}
    res.sort()
    start = [0,0]
    for i in range(n): 
        a[i] = []
        end = [9 + (i*t//60), (0 + i*t) % 60]
        for H,M in res:
            if (H > start[0] or (H == start[0] and M > start[1])) and  (H < end[0] or (H == end[0] and M <= end[1])):
                a[i].append((H,M))
        start = copy.deepcopy(end)

    ex = 0
    for val in a.values():
        if len(val) > m + ex:
            ex += len(val) - m - ex
        else:
            ex -=  m -len(val)
    print(a)
    print(ex)
    if ex < 0: return str(end[0]).zfill(2) + ":" + str(end[1]).zfill(2)
    else:
        total = len(timetable) - sum([len(i) for i in a.values()])
        answer = res[-ex-1-total]
        if answer[1] == 0:
            return str(answer[0]-1).zfill(2) + ":" + str(59)
        return str(answer[0]).zfill(2) + ":" + str(answer[1]-1).zfill(2)



print(solution(	1, 10, 1, ["09:10", "09:09","09:00", "08:00"]))
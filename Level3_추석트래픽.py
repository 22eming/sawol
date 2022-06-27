def solution(lines):
    start, end = [], []
    for line in lines:
        d, t, p = line.split()
        h, m, s = map(float, t.split(":"))
        
        p = float(p[:-1])
        seconds = h * 3600 + m * 60 + s
        
        start.append(seconds - p + 0.001)
        end.append(seconds+1)
    
    start.sort()
    answer = 1
    cur_traf, max_traf = 0, 0
    cnt_s, cnt_e = 0, 0
    
    while cnt_s < len(lines) and cnt_e < len(lines):
        if start[cnt_s] < end[cnt_e]:
            cur_traf += 1
            max_traf = max(cur_traf, max_traf)
            cnt_s += 1
        else:
            cnt_e += 1
            cur_traf -= 1
    
    return max_traf


print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))

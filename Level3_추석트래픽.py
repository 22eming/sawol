def solution(lines):
    answer = 0
    log = []
    for line in lines:
        (day, time, dt) = line.split(" ")
        (h, m, s) = time.split(":")

        t = float(h)*3600 + float(m)*60 + float(s)
        dt = float(dt[:-1])

        start = t-dt+0.001
        end = t+1

        log.append([start, end])

    idx = 0
    for start, end in log:
        cnt = 0
        for s, e in log[idx:]:
            if end > s:
                cnt += 1
            if end+4 < e:
                break
        answer = max(cnt, answer)
        idx += 1
    return answer


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

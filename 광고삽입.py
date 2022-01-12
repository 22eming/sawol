def str_to_int(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def int_to_str(t):
    h = str(t//3600).rjust(2,"0")
    m = str(t%3600//60).rjust(2,"0")
    s = str(t%60).rjust(2,"0")
    return h+":"+m+":"+s

def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    timeline = [0]*(play_time+1)
    for log in logs:
        timeline[str_to_int(log[:8])] += 1
        timeline[str_to_int(log[9:])] -= 1
    
    for i in range(1,play_time+1):
        timeline[i] = timeline[i] + timeline[i-1]

    for i in range(1,play_time+1):
        timeline[i] = timeline[i] + timeline[i-1]

    max_viewer = 0
    max_time = 0
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if max_viewer < timeline[i] - timeline[i-adv_time]:
                max_viewer = timeline[i] - timeline[i-adv_time]
                max_time = i -adv_time +1
        else:
            if max_viewer < timeline[i]:
                max_viewer = timeline[i]
                max_time = i-adv_time +1

    return int_to_str(max_time)

print(solution("99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
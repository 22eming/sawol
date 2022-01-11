def solution(dirs):
    answer = 0
    way = {'U':(-1,0), 'D':(1,0), 'R':(0,1), 'L':(0,-1)}
    visit = set()
    y, x = 0, 0
    for d in dirs:
        dy, dx = way[d]
        if abs(y+dy) > 5 or abs(x+dx) > 5:
            continue
        else:
            if (y,x,y+dy,x+dx) not in visit and (y+dy,x+dx,y,x) not in visit:
                answer += 1
                visit.add((y,x,y+dy,x+dx))
            y, x = y+dy, x+dx
    return answer


print(solution("ULURRDLLU"))
# 0,0 시작 (-5,-5)


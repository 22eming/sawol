def check(answer):
    for x,y,a in answer:
        if a == 0:
            if y == 0:
                continue
            elif ([x, y-1, 0] not in answer) and ([x-1, y, 1] not in answer) and ([x,y,1] not in answer):
                return False
        else:
            if ([x+1,y-1,0] not in answer) and ([x,y-1,0] not in answer) and ( [x-1,y,1] not in answer or [x+1,y,1] not in answer ):
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x,y,a,b in build_frame:
        if b == 1: #설치
            if a == 0: # 기둥
                # 자신 밑에 기둥이나 보가 있을때
                if ([x,y-1,0] in answer) or ([x-1,y,1] in answer) or ([x,y,1] in answer) or y == 0:
                    answer.append([x,y,a])
            elif a == 1: # 보
                # 자신 양밑에 기둥이 있거나 양옆에 보가 있을때
                if ([x,y-1,0] in answer) or ([x+1,y-1,0] in answer)  or ( [x-1,y,1] in answer and [x+1,y,1] in answer ):
                    answer.append([x,y,a])
        else: #삭제
            answer.remove([x,y,a])
            if check(answer) == False:
                answer.append([x,y,a])
                
    return sorted(answer)


print(solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]] ))

#[X,Y,(0:기둥, 1:보), (0:삭제, 1: 설치) ]
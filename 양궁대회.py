from collections import defaultdict
from itertools import combinations

def solution(n, info):
    answer = [0]*11
    info.reverse()
    data = defaultdict(list)
    # 같은 이득값을 갖는 점수끼리 모음
    for k in range(n, 0,-1):
        for com in combinations((10,9,8,7,6,5,4,3,2,1,0), k):
            com, s, cnt = list(com), 0, n
            for c in com:
                cnt -= info[c]+1
                s += c
                if info[c] != 0:
                    s += c
            if cnt >= 0:
                if cnt > 0:
                    com.append(0)
                com.reverse()
                data[s].extend([com]) 


    # 가장 작은 수를 더 많이 맞춘 경우
    data_min = sorted(data[max(data.keys())])
    
    # 화살 개수 추가
    for d in  data_min[0][::-1]:
        answer[d] += info[d]+1
        if d == 0:
            answer[d] += n - sum(answer)
            
    # 라이언이 어피치에게 졌을 때
    result = 0
    for i in range(11):
        if info[i] > answer[i]:
            result -= i
        elif info[i] < answer[i]:
            result += i
    if result <= 0:
        return [-1]

    answer.reverse()
    return answer



# 발당 평균 이득값을 계산하여 가장 높은 이득값
# 같은 이득값일때는 가장 낮은 점수
# 이득값, 소요 화살, 낮은 점수
# print(solution(9,	[0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(5,	[2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(4,	[3,0,0,0,0,1,0,0,0,0,0]))
print(solution(1,	[1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(10,	[0,0,0,0,0,0,0,0,3,4,3]))
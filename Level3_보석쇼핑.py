from bisect import bisect_left
def solution(gems):
    dic = {}
    list_gems = len(set(gems))
    answer = []
    res = [0,len(gems)]
    for i in range(len(gems)):
        if dic.get(gems[i]):
            del answer[bisect_left(answer, dic[gems[i]])]
        dic[gems[i]] = i+1
        answer.append(i+1)
        if len(answer) == list_gems:
            if res[1] - res[0] > answer[-1] - answer[0]:
                res = [answer[0], answer[-1]]
    return res


print(solution( ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] ))

from typing import DefaultDict


def solution(tickets):
    dic = DefaultDict(list)
    for s, a in tickets:
        dic[s].append(a)
    for s in dic.keys():
        dic[s].sort()

    stack = ['ICN']
    visit = []
    while stack:
        cur_p = stack[-1]
        if dic[cur_p] != []:
            stack.append(dic[cur_p].pop(0))
        else:
            visit.append(stack.pop())
    visit.reverse()
    return visit


t = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]

print(solution(t))

# visit의 마지막이 지금 위치
# 출발했을때 그 위치의 공항이 출발인 티켓이 있는지 재귀로 확인
# 없다면 돌아온다.

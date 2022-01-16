import numpy as np


def solution(n, costs):
    answer = 0
    visit = np.zeros(n)
    costs = sorted(costs, key=lambda x: x[2])
    cnt = 1
    for l_node, r_node, cost in costs:
        if visit[l_node] == 0 and visit[r_node] == 0:
            visit[l_node] = cnt
            visit[r_node] = cnt
            cnt += 1
        elif visit[l_node] == visit[r_node]:
            continue
        elif visit[l_node] > 0 and visit[r_node] > 0:
            visit = np.where(visit == visit[r_node], visit[l_node], visit)
        else:
            if visit[l_node] == 0:
                visit[l_node] = visit[r_node]
            else:
                visit[r_node] = visit[l_node]
        answer += cost

    return answer


answer = [
    [5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]],  # 8
    [6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1],  # 11
         [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]],
    [5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]],  # 6
    [5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]],  # 8
]
for i in answer:
    print(solution(i[0], i[1]))

import numpy as np
from collections import defaultdict


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])

    for i in range(1, n + 1):
        # i가 진 선수들
        for winner in lose[i]:
            # i 에게 진 선수들 업데이트
            win[winner].update(win[i])
        # i가 이긴 선수들
        for loser in win[i]:
            # i 에게 이긴 선수들 업데이트
            lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer


# def solution(n, results):
#     m = np.zeros((n, n))
#     for win, lose in results:
#         m[win-1][lose-1] = 1
#         m[lose-1][win-1] = -1

#     for k in range(0, n):
#         for a in range(0, n):
#             for b in range(0, n):
#                 if m[a][k] == m[k][b]:
#                     m[a][b] = m[a][k] if m[a][k] != 0 else m[a][b]

#     answer = sum([1 for i in m if list(i).count(0) == 1])
#     return answer


print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5, 6], [6, 7]]))

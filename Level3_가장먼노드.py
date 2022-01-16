import numpy as np
from collections import deque


def bfs(grape, cur, answer):
    visited = list(np.zeros(len(grape)+1))
    queue = deque([cur])
    visited[cur] = 1

    while queue:
        q = queue.popleft()
        for i in grape[q]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                answer[i] = answer[q] + 1
    return answer


def solution(n, edge):
    grape = dict([(i, []) for i in range(1, n+1)])
    for v1, v2 in edge:
        grape[v1].append(v2)
        grape[v2].append(v1)

    answer = bfs(grape, 1, np.zeros(n+1))
    answer = np.where(answer == max(answer))[0]
    return len(answer)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

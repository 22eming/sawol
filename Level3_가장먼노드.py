import numpy as np
from collections import deque


def bfs(grape, cur, answer):
    que = deque([cur])
    visited = [0] * (len(grape)+1)
    visited[cur] = 1
    
    while que:
        q = que.popleft()
        for i in grape[q]:
            if not visited[i]:
                visited[i] = 1
                que.append(i)
                answer[i] = answer[q] + 1
                
    return answer

def solution(n, edge):
    grape = dict([[i, []] for i in range(1, n+1)])
    for v1, v2 in edge:
        grape[v1].append(v2)
        grape[v2].append(v1)
        
    res = bfs(grape, 1, np.zeros(n+1))
    return len(np.where(res == max(res))[0])


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

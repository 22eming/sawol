from collections import defaultdict
from collections import deque
from turtle import right


def solution(info, edges):
    answer = 0
    node = defaultdict(list)

    for p, c in edges:
        node[p].append(c)

    sheep, wolf, s_and_w = [], [], []
    stack = deque([0])
    while stack:
        n = stack.popleft()
        left, right = node[n]
        # 양 양
        if info[left] == 0 and info[right] == 0:
            pass
        # 늑대 늑대
        elif info[left] == 1 and info[right] == 1:
            pass
        # 양 늑대
        else:
            pass

    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [
      0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
# 양 늑대
# 양 양
# 늑대 늑대

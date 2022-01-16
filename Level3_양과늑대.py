from collections import defaultdict
from collections import deque


def solution(info, edges):
    answer = 0
    node = defaultdict(list)
    for p, c in edges:
        node[p].append(c)

    stack = deque([0])
    print(stack.popleft())
    print(stack)
    sheep, wolf, s_and_w = [], [], []
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [
      0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
# 양 늑대
# 양 양
# 늑대 늑대

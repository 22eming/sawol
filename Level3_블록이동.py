import numpy as np
from collections import deque


def bfs(board, p1, p2):
    # 상하좌우 이동....
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visit = []
    for dy, dx in move:
        p11 = (p1[0]+dy, p1[1]+dx)
        p22 = (p2[0]+dy, p2[1]+dx)
        if board[p11[0]][p11[1]] == 0 and board[p22[0]][p22[1]] == 0:
            visit.append((p11, p22))

    # 회전
    if p1[0] == p2[0]:  # 가로
        for i in [1, -1]:
            if board[p1[0]+i][p1[1]] == 0 and board[p2[0]+i][p2[1]] == 0:
                visit.append((p1, (p1[0]+i, p1[1])))
                visit.append((p2, (p2[0]+i, p2[1])))
    else:
        for i in [1, -1]:
            if board[p1[0]][p1[1]+i] == 0 and board[p2[0]][p2[1]+i] == 0:
                visit.append((p1, (p1[0], p1[1]+i)))
                visit.append((p2, (p2[0], p2[1]+i)))
    return visit


def solution(board):
    end = len(board)
    board = np.pad(np.array(board), ((1, 1), (1, 1)),
                   'constant', constant_values=1)

    que = deque([((1, 1), (1, 2), 0)])
    visit = set([((1, 1), (1, 2))])
    while que:
        f, b, cnt = que.popleft()
        if f == (end, end) or b == (end, end):
            return cnt
        for x in bfs(board, f, b):
            if x not in visit:
                que.append((x[0], x[1], cnt+1))
                visit.add(x)


answer = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]
print(solution(answer))

# [[1 1 1 1 1 1 1 1 1 1 1]
#  [1 0 0 0 0 0 0 0 0 0 1]
#  [1 1 1 1 1 1 1 1 0 0 1]
#  [1 1 1 1 1 1 1 1 1 0 1]
#  [1 0 0 0 0 0 0 0 0 0 1]
#  [1 0 0 1 1 1 1 1 0 0 1]
#  [1 0 1 1 1 1 1 1 1 1 1]
#  [1 0 0 1 1 1 1 1 0 0 1]
#  [1 0 0 0 0 0 0 0 0 0 1]
#  [1 1 1 1 1 1 1 1 1 0 1]
#  [1 1 1 1 1 1 1 1 1 1 1]]

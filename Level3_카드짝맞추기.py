from typing import DefaultDict
from collections import deque
import numpy as np
from itertools import permutations
from copy import deepcopy

from numpy.testing._private.utils import print_assert_equal


def cal(board, card, pro, r, c):
    # now 와 want의 최소 거리
    def bfs(now, want):
        que = deque([[now, 0]])
        d = ((-1, 0), (0, 1), (1, 0), (0, -1))
        visit = []
        while que:
            q, cnt = que.popleft()
            if q == want:
                return cnt
            if q not in visit:
                visit.append(q)
                # 상하좌우 +1
                for dy, dx in d:
                    y = q[0] + dy
                    x = q[1] + dx
                    if board[y][x] != -1:
                        que.append([[y, x], cnt+1])
                # ctrl 가로
                ctrl = [i for i in card_list if i[0] == q[0]]
                dx = [i[1] for i in ctrl if i[1] < q[1]]
                if dx:
                    que.append([[q[0], max(dx)], cnt+1])
                else:
                    que.append([[q[0], 1], cnt+1])
                dx = [i[1] for i in ctrl if i[1] > q[1]]
                if dx:
                    que.append([[q[0], min(dx)], cnt+1])
                else:
                    que.append([[q[0], 4], cnt+1])
                # ctrl 세로
                ctrl = [i for i in card_list if i[1] == q[1]]
                dy = [i[0] for i in ctrl if i[0] < q[0]]
                if dy:
                    que.append([[max(dy), q[1]], cnt+1])
                else:
                    que.append([[1, q[1]], cnt+1])
                dy = [i[0] for i in ctrl if i[0] > q[0]]
                if dy:
                    que.append([[min(dy), q[1]], cnt+1])
                else:
                    que.append([[4, q[1]], cnt+1])
    result = 0
    # 순서대로 찾기
    for i in pro:
        card_list = [x for i in list(card.values()) for x in i]
        l_cnt = bfs([r, c], card[i][0]) + bfs(card[i][0], card[i][1])
        r_cnt = bfs([r, c], card[i][1]) + bfs(card[i][1], card[i][0])
        [r, c] = card[i][1] if l_cnt < r_cnt else card[i][0]
        result += min(l_cnt, r_cnt)
        # 보드에서 삭제
        for j in card[i]:
            board[j[0]][j[1]] = 0
        # card에서 삭제
        del card[i]
    return result


def solution(board, r, c):
    answer = 10**9
    card = DefaultDict(list)
    board = np.pad(board, ((1, 1), (1, 1)), constant_values=-1)
    for y in range(6):
        for x in range(6):
            if board[y][x] > 0:
                card[board[y][x]].append([y, x])

    for i in permutations(list(card.keys())):
        dc = deepcopy(card)
        answer = min(answer, cal(board, dc, i, r+1, c+1))
    return answer + len(list(card.keys()))*2


print(solution([[0, 0, 1, 0], [1, 0, 0, 0], [4, 4, 3, 2], [0, 3, 2, 0]],	2,	0))

# 모든 카드 경우의 수를 다 해본다
# 하나 삭제 할 때마다 다음 카드 계산

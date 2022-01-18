from copy import copy
import numpy as np

# 4방향으로 이동한 보드, pos값으로 재귀
# 만약 이동이 불가능하면 승패와 cnt리턴
# 만약 모든 승패 리턴 값이 동일하면 '확정된 결과'
# 승리하는 플레이어는 최소한의 이동
# 패배하는 플레이어는 최대한의 이동

def a_turn(board, apos, bpos, cnt):
    # a 패배
    if board[apos[0], apos[1]] == 0:
        return 1, cnt-1

    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
    b = copy(board)
    b[apos[0],apos[1]] = 0
    save = []
    con = []
    for i in range(4):
        # 결과값 : 확정, 승, 패
        # 확정: 승리 확정 -> 최소값, 패배 확정 -> 최대값
        # 승패: 전체 결과가 같으면 확정
        if 0 <= apos[0] + dy[i] < len(board) and 0 <= apos[1] + dx[i] < len(board[0]):
            save.append(b_turn(b, [apos[0]+dy[i], apos[1]+dx[i]], bpos))

    # 확정된 B 승리
    if all(map(lambda x: x[0] == 1, save)) :
        return 5, max([i[1] for i in save])
    # 확정된 a 승리
    elif all(map(lambda x: x[0] == 0, save)):
        return -5, min([i[1] for i in save])
    # 확정


def b_turn(board, apos, bpos, cnt):

    return 0


def solution(board, aloc, bloc):
    answer = -1
    board = np.array(board)
    a_turn(board, aloc)
    return answer


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2]))
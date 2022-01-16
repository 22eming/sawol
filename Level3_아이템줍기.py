import numpy as np


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 최대 맵 크기
    max_y = [max([i[3] for i in rectangle])+1,
             max([i[2] for i in rectangle])+1]

    # 맵 생성
    board = np.ones((max_y[0]*2, max_y[1]*2))
    for i in rectangle:
        x1, x2, y1, y2 = i[0]*2, i[2]*2, i[1]*2, i[3]*2
        rec = np.full((y2-y1-1, x2-x1-1), -1)
        rec = np.pad(rec, ((1, 1), (1, 1)), 'constant', constant_values=-2)
        board[y1:y2+1, x1:x2+1] = board[y1:y2+1, x1:x2+1] * rec
        board[board == 2] = -1
        board[board == 4] = -2

    # dfs 탐색
    cnt = 0
    cur_p = [[characterY*2, characterX*2]]
    visited = np.zeros((max_y[0]*2, max_y[1]*2))
    visited[cur_p[0][0]][cur_p[0][1]] = 1
    while cur_p:
        cnt += 1
        cur = cur_p.pop(-1)
        visited[cur[0]][cur[1]] = 1
        for i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            y, x = cur[0]+i[0], cur[1]+i[1]
            if board[y][x] == -2 and visited[y][x] == 0:
                cur_p.append([y, x])
        if cur == [itemY*2, itemX*2]:
            answer = cnt
    # min(방향1, 방향2)
    return min(cnt-answer, answer)//2


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [
      4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))

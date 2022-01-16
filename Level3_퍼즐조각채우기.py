import numpy as np


def make_puzzle(board, num, visited, pos):
    puzzle = [pos]
    stack = [pos]
    min_y, min_x, max_y, max_x = 50, 50, 0, 0
    while stack:
        p = stack.pop()
        visited[p[0]][p[1]] = 1
        min_y = min(min_y, p[0])
        min_x = min(min_x, p[1])
        max_y = max(max_y, p[0])
        max_x = max(max_x, p[1])
        for i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            y, x = p[0]+i[0], p[1]+i[1]
            if board[y][x] == num and visited[y][x] == 0:
                stack.append([y, x])
                puzzle.append([y, x])
    puz_map = np.zeros((max_y-min_y+1, max_x-min_x+1))
    for p in puzzle:
        puz_map[p[0]-min_y][p[1]-min_x] = 1
    return puz_map, visited


def make_list(input_board, num):
    board = np.pad(np.array(input_board), ((1, 1), (1, 1)),
                   'constant', constant_values=-1)
    visited = np.zeros((len(input_board)+2, len(input_board)+2))
    board_idx = np.where(board == num)
    game_list = []
    for i in zip(board_idx[0], board_idx[1]):
        if visited[i[0]][i[1]] == 0:
            puzzle, visited = make_puzzle(board, num, visited, i)
            game_list.append(puzzle)
    return game_list


def solution(game_board, table):

    answer = 0
    game_list = make_list(game_board, 0)
    table_list = make_list(table, 1)
    for tl in table_list:
        for _ in range(4):
            tl = np.rot90(tl)
            for i, g in enumerate(game_list):
                if np.array_equal(tl, g):
                    answer += int(np.sum(tl))
                    del game_list[i]
                    break
            else:
                continue
            break

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
# 아이디어
# input_board에서 0 or 1이 발견 되면 visited인지 확인
# 방문 안한 곳이면 함수 통해 도형 리턴
# game_board와 table에서 도형이 모두 완성 되었다면
# table 도형을 하나씩 꺼내와서 4번 회전 시키며 같은게 있는지 확인

def check_ceil(row, x):
    global Board
    for y in range(row):
        if Board[y][x] != 0:
            return False
    return True


def nXn(row, col, h, w):
    global Board
    zero_cnt, val = 0, -1
    for y in range(row, row+h):
        for x in range(col, col+w):
            if Board[y][x] == 0:
                if not check_ceil(y,x):
                    return False
                zero_cnt += 1
                if zero_cnt > 2:
                    return False
            else:
                if val == -1:
                    val = Board[y][x]
                elif val != Board[y][x]:
                    return False

    for y in range(row, row+h):
        for x in range(col, col+w):
            Board[y][x] = 0
    return True


Board = []
def solution(board):
    global Board
    Board = board
    answer, n = 0, len(board)
    while True:
        cnt = 0
        for y in range(n):
            for x in range(n):
                if y <= n-2 and x <= n-3 and nXn(y, x, 2, 3):
                    cnt += 1
                elif y <= n-3 and x <= n-2 and nXn(y, x, 3, 2):
                    cnt += 1
        if cnt == 0:
            break
        answer += cnt
    return answer

s = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 3, 0, 4, 8, 8, 0],
    [0, 0, 0, 2, 3, 4, 4, 4, 0, 0],
    [1, 2, 2, 2, 3, 3, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]

print(solution(s))
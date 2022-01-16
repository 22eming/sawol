from collections import deque
import sys


def solution(board):
    def bfs(s):
        answer = sys.maxsize
        di = ((-1, 0), (0, 1), (1, 0), (0, -1))
        n = len(board)
        visited = [[sys.maxsize]*n for _ in range(n)]
        visited[0][0] = 0

        stack = deque([s])  # y, x, d, cost
        while stack:
            y, x, d, cost = stack.popleft()
            for i in range(4):
                dy, dx = y + di[i][0], x + di[i][1]

                if 0 <= dx < n and 0 <= dy < n:
                    if board[dy][dx] == 0:
                        dc = cost+100 if i == d else cost+600
                        if dc < visited[dy][dx]:
                            visited[dy][dx] = dc
                            stack.append([dy, dx, i, dc])
        return visited[-1][-1]
    return min(bfs((0, 0, 1, 0)), bfs((0, 0, 2, 0)))


board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0]
]
print(solution(board))

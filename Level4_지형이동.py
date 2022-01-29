import heapq
import numpy as np
def solution(land, height):
    n = len(land)
    answer = 0
    d = ((-1,0), (0,1), (1,0), (0,-1))

    heap = [(0,0,0)]
    total, cnt = n*n, 0
    board = np.full((n,n), False)

    while cnt < total:
        dif, y, x = heapq.heappop(heap)
        if board[y,x] != False:
            continue

        board[y,x] = True
        answer += dif
        cnt += 1

        now_dif = land[y][x]
        for dy, dx in d:
            dy, dx = y+dy, x+dx
            if 0 <= dy < n and 0 <= dx < n:
                d_dif = land[dy][dx]
                if abs(now_dif - d_dif) > height:
                    heapq.heappush(heap, (abs(now_dif - d_dif),dy,dx))
                else:
                    heapq.heappush(heap, (0,dy,dx))

    return answer

# print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1))
print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))
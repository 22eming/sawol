# import numpy as np

# def solution(N, road, K):
#     answer = 0
#     board = np.full((N+1,N+1), np.inf)
#     for city_a,city_b,time in road:
#         t = min(board[city_a][city_b], time)
#         board[city_a][city_b] = t
#         board[city_b][city_a] = t
#     # 경유지
#     for i in range(1, N+1):
#         board[i][i] = 0
#         #출발지
#         for j in range(1, N+1):
#             #목적지
#             for k in range(1, N+1):
#                 board[i][j] = min(board[i][j], board[i][k]+board[k][j] )
#     return len(board[1][board[1]<=K])


from collections import deque

def solution(N, road, K):
    cost = [10e6]*(N+1)
    cost[1] = 0
    stack = deque([1])
    while stack:
        start = stack.popleft()
        for city_a, city_b, time in road:
            if city_a == start or city_b == start:
                arrive = city_b if city_a == start else city_a
                if cost[arrive] > cost[start]+time:
                    cost[arrive] = cost[start]+time
                    stack.append(arrive)
    return len([1 for i in cost if i <= K ])


print(solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	,4))
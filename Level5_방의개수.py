from collections import defaultdict


def solution(arrows):
    answer = 0
    visited = defaultdict(list)
    y, x = 0, 0
    dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)

    cur = '0_0'
    for move in arrows:
        next_move = (move+4)%8
        # x 교차점 예외 때문에 2칸씩
        for _ in range(2):
            ny, nx = y + dy[move], x + dx[move]
            next = '{0}_{1}'.format(ny,nx)
            # 노드 방문 AND 경로 방문
            if next in visited and next_move not in visited[next]:
                answer += 1
                visited[cur].append(move)
                visited[next].append(next_move)
            # 노드 미방문
            elif next not in visited:
                visited[cur].append(move)
                visited[next].append(next_move)
            y, x = ny, nx
            cur = next
            
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))

# dic[y_x] = [F, []]
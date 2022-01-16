maxsize = 1000000


def solution(n, s, a, b, fares):
    mat = [[maxsize]*(n+1) for _ in range(n+1)]

    for fare in fares:
        node1, node2, cnt = fare
        mat[node1][node2] = cnt
        mat[node2][node1] = cnt

    for k in range(1, n+1):
        mat[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                x = mat[i][k] + mat[k][j]
                if mat[i][j] > x:
                    mat[i][j] = x

    return min([mat[mid][s] + mat[mid][a] + mat[mid][b] for mid in range(1, n+1)])


print(solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

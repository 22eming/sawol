def solution(n, m, x, y, queries):
    x1, x2, y1, y2 = y, y, x, x  # x가 행.. y가 열..
    for d, cnt in reversed(queries):
        if d == 0:
            if x1 != 0:
                x1 += cnt
            x2 = x2+cnt if x2+cnt < m-1 else m-1
            if x1 > m:
                return 0
        elif d == 1:
            if x2 != m-1:
                x2 -= cnt
            x1 = x1-cnt if x1-cnt > 0 else 0
            if x2 < 0:
                return 0
        elif d == 2:
            if y1 != 0:
                y1 += cnt
            y2 = y2+cnt if y2+cnt < n-1 else n-1
            if y1 > n:
                return 0
        elif d == 3:
            if y2 != n-1:
                y2 -= cnt
            y1 = y1-cnt if y1-cnt > 0 else 0
            if y2 < 0:
                return 0
    return (x2-x1+1)*(y2-y1+1)
# 목적지에서 역순으로 계산


print(solution(2,	5,	0,	1,	[[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))

def solution(mat):
    n = len(mat)
    dp = [ [float('inf')]*n for _ in range(n)]

    for idx in range(n):
        dp[idx][idx] = 0

    for gap in range(1, n):
        for start in range(n-gap):
            if gap == 1: # gap이 1일 때
                dp[start][start+1] = mat[start][0] * mat[start][1] * mat[start+1][1]
                continue
            end = start + gap
            for station in range(start, end):
                dp[start][end] = min(dp[start][end],
                                dp[start][station] + dp[station+1][end] + (mat[start][0] * mat[station][1] * mat[end][1]) )

    return dp[0][-1]

# dp[s][e] 의 최소값?
    # dp[s][중간값] + dp[중간값+1][e] + (중간값 합치는 비용)

print(solution([[5,3],[3,10],[10,6]]))

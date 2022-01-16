def solution(m, n, puddles):
    dp = [[1 for j in range(m)] for i in range(n)]
    for x,y in puddles:
        dp[y-1][x-1] = 0
        if y == 1:
            dp[y-1][x-1:] = [0]*(m-x+1)
        if x == 1:
            for i in range(y-1,n): dp[i][0] = 0  

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == 0: continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1] % 1000000000


print(solution(5,4,[[2,1],[1,2]]))


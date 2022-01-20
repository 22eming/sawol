def d(money):
    dp = {}
    dp[0] = money[0]
    dp[1] = max(money[:2])
    for i in range(len(money) - 2):
        dp[i + 2] = max( dp[i+1], dp[i] + money[i+2] )
    return dp

def solution(money):
    return max( d(money[:-1])[len(money) - 2], d(money[1:])[len(money) - 2]  )

print(solution([1, 2, 3, 1]))
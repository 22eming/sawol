from collections import defaultdict


def solution(sales, links):
    sales = [0] + sales
    dp = {}
    team = defaultdict(list)

    for a, b in links:
        team[a].append(b)
        dp[a] = [0,0]

    def dfs(cur):
        if cur not in team:
            dp[cur] = [sales[cur], 0]
            return None
        
        min_cost = 10000
        dp[cur][0] = sales[cur]
        for i in team[cur]:
            dfs(i)
            dp[cur][0] += min(dp[i])
            min_cost = min(min_cost, dp[i][0] - dp[i][1])
        if min_cost < 0: min_cost = 0
        dp[cur][1] = dp[cur][0] - sales[cur] + min_cost

    dfs(1)
    return min(dp[1])

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
	[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))

# 모든 팀은 최소 1명 이상의 직원.
# 참석하는 직원들의 하루평균 매출액의 합이 최소.

# 최소값 판별할때 팀원이자 팀장인지 확인
# 직원이 너무 많음 완전 탐색 불가능
def d(sticker):
    dp = {}
    dp[0] = sticker[0]
    dp[1] = max(sticker[:2])
    for i in range(len(sticker) - 2):
        dp[i + 2] = max(dp[i + 1], dp[i] + sticker[i + 2])
    return dp


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    return max(d(sticker[:-1])[len(sticker) - 2], d(sticker[1:])[len(sticker) - 2])



    

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
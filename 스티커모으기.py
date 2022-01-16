def solution(sticker):
    n = len(sticker)

    dp = [0] * n
    if n<3:
        return max(sticker)
    dp[:2] = sticker[:2]    
    dp[2] = max(sticker[1], sticker[0]+sticker[2])
    if n == 3:
        return max(dp)
    
    for i in range(3, n-1):
        dp[i] = max(dp[i-3] + sticker[i], dp[i-2] + sticker[i], dp[i-1] ) # 0+3, 1+3, 2

    dp2 = [0] * n
    dp2[0]=0
    dp2[1]=sticker[1]
    dp2[2]=max(sticker[1], sticker[2])
    for i in range(3, n):
        dp2[i] = max(dp2[i-3] + sticker[i], dp2[i-2] + sticker[i], dp2[i-1] )

    return max(max(dp), max(dp2))



    

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
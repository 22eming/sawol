def solution(N, number):
    dp = [[]]
    
    for i in range(1, 9):
        dp.append(set())
        dp[i].add(int(str(N)*i))
        
        for j in range(i):
            for para1 in dp[j]:
                for para2 in dp[i-j]:
                    dp[i].add(para1 + para2)
                    dp[i].add(para1 - para2)
                    dp[i].add(para1 * para2)
                    if para2 != 0:
                        dp[i].add(para1 // para2)

            if number in dp[i]:
                return i
    
    return -1


print(solution(2, 11))
def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[i-j] * dp[j-1]
    return dp[-1]

print(solution(3))

## 카타란 수

#[C4를 구하는 방법]

# () {3쌍의 괄호}   = 경우의 수 C0*C3
# ({1쌍의 괄호}) {2쌍의 괄호}   = 경우의 수 C1*C2

# ({2쌍의 괄호}) {1쌍의 괄호} = 경우의 수 C2*C1

# ({3쌍의 괄호})  = 경우의 수 C3*C0

# C4 = C0*C3 + C1*C2 + C2*C1 + C3*C0 = 5+2+2+5 = 14
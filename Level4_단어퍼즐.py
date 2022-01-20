from collections import defaultdict

def solution(strs, t):
    dp = [0] * (len(t)+1)
    str_dic = defaultdict(set)
    for s in strs:
        str_dic[s[-1]].add(s)

    for i in range(1, len(t)+1):
        dp[i] = float('inf')
        if str_dic[t[i-1]]:
            for j in range(1,6):
                if i - j < 0:
                    s = 0
                else:
                    s = i-j
                if t[s:i] in str_dic[t[i-1]]:
                    dp[i] = min(dp[i], dp[s]+1)

    return -1 if dp[-1] == 'inf' else dp[-1]
    





# print(solution(["ba","na","n","a"],	"banana"))
# print(solution(["app","ap","p","l","e","ple","pp"],	"apple"))
print(solution(["ba","an","nan","ban","n"],	"banana"))
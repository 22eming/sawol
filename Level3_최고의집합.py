def solution(n, s):
    if n > s: return [-1]
    x,y = divmod(s,n)
    answer = [x]*(n-y) + [x+1]*y
    return answer


print(solution(3,8))

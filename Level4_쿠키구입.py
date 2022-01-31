def cal(l, r, cookie, n):
    answer = 0
    left, right = cookie[l], cookie[r]
    while True:

        if left == right:
            answer = left
            if l == 0 or r == n:
                return answer
            else:
                l -= 1
                r += 1
                left += cookie[l]
                right += cookie[r]

        elif left > right:
            if r == n:
                return answer
            else:
                r += 1
                right += cookie[r]

        else: # left < right
            if l == 0:
                return answer
            else:
                l -= 1
                left += cookie[l]


def solution(cookie):
    answer = 0
    n = len(cookie)-1
    for i in range(n):
        answer = max(answer, cal(i, i+1, cookie, n))
            
    return answer

print(solution([1,2,4,5]))
print(solution([1,1,2,3]))
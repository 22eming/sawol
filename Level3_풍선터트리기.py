def solution(a):
    answer = 0
    left_min = a[0]; right_min = a[-1]
    min_idx = a.index(min(a))
    for i in a[:min_idx]:
        if left_min >= i:
            left_min = i
            answer += 1
    for i in a[:min_idx:-1]:
        if right_min >= i:
            right_min = i
            answer += 1
    return answer+1

# 최저값
# 최저값을 터트릴 때
print(solution([9,-1,-5]))

# [--] 최저값 [++]

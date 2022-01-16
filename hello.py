def solution(nums):
    a = list(set(nums))
    if len(nums)/2 >= len(a):
        return len(a)
    else:
        return int(len(nums)/2)

print(solution([3,3,3,2,2,4]))

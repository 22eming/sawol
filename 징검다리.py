def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 0, distance
    while start <= end:
        mid = (start+end)//2
        last_value = 0
        cnt = 0

        for i in range(len(rocks)-1):
            interval = rocks[i]-last_value
            if interval >= mid:
                cnt += 1
                last_value = rocks[i]

        # 마지막 징검다리 검사
        if rocks[-1] - last_value >= mid and distance - rocks[-1] >= mid:
            cnt += 1

        if cnt >= len(rocks) - n:
            start = mid+1
            answer = mid
        else:
            end = mid - 1

    return answer

print(solution(25,	[2, 14, 11, 21, 17],	2))
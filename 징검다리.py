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
# len(rocks)개의 바위가 있고 그 중 n 개의 바위를 삭제함
# 시작 바위 끝의 거리의 최소값을 리턴

# 풀이
## 바위끼리의 거리값을 담는 리스트 생성
## 연결리스트로 앞뒤를 연결하고 삭제할때마다 삭제한 바위와 연결된 리스트 값 변경
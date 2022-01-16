from collections import Counter


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    # food_items 시간순으로 등장횟수 정렬
    counter = sorted(Counter(food_times).items())
    # food_time 길이, 제거된 시간 개수, 넘어간 초, 저번 count값
    food_lenth, n, answer, last_count = len(food_times), 0, 0, 0
    for count in counter:
        # count[0] 시간짜리 음식 먹는데 소요되는 시간
        tmp = (food_lenth - n) * (count[0] - last_count)
        # 총 소요시간이 방송 중단시간보다 큰가
        if tmp + answer > k:
            break
        n += count[1]
        last_count = count[0]
        answer +=  tmp
    # 방송 중단까지 남은 음식 수
    k = (k - answer) % (food_lenth - n)
    for i in range(food_lenth):
        if food_times[i] >= count[0]:
            k -= 1
            if k < 0:
                return i+1

print(solution([7,8,3,3,2,2,2,2,2,2,2,2],29))
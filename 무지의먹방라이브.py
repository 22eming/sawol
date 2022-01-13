from collections import Counter


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    counter = sorted(Counter(food_times).items())
    food_lenth, n, answer, cnt = len(food_times), 0, 0, 0
    for count in counter:
        tmp = (food_lenth - n) * (count[0] - cnt)
        if tmp + answer > k:
            break
        n += count[1]
        cnt = count[0]
        answer +=  tmp
    print("answer:{0}   len:{1}".format(answer, food_lenth-n))
    k = ( k - answer) % (food_lenth - n)
    print(k)
    # if k == 0:
    #     for i in range(food_lenth):
    #         if food_times[i] >= count[0]:
    #             return i+2

    for i in range(food_lenth):
        if food_times[i] >= count[0]:
            k -= 1
            if k < 0:
                return i+1

# print(solution([1, 3, 2], 5))
# print(solution([3,4,5,6,2],7))
# print(solution([4,1,1,5],4))
# print(solution([1,100],10))
print(solution([7,8,3,3,2,2,2,2,2,2,2,2],28))
print()
print(solution([7,8,3,3,2,2,2,2,2,2,2,2],29))
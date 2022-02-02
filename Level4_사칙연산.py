def solution(arr):
    temp, sum_num = {'min':0, 'max':0}, 0
    for i in range(-1, -len(arr)-1, -1):
        if arr[i] >= "0":
            sum_num += int(arr[i])
        elif arr[i] == "-":
            temp['min'], temp['max'] = min( temp['min'] - sum_num, -(temp['max'] + sum_num)), max( -(temp['min'] + sum_num), temp['max'] + sum_num - int(arr[i+1])*2 ) # 중간값을 묶어 -하나? 따로 - 하나 차이
            sum_num = 0

    return temp["max"] + sum_num

print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
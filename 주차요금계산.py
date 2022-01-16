from collections import defaultdict
from math import ceil

def str_to_min(time):
    h,m = time.split(":")
    return int(h)*60 + int(m)

def solution(fees, records):
    answer = []
    basic_m, basic_w, unit_m, unit_w = fees
    data_inout = {}
    data_time = defaultdict(int)
    for record in records:
        time, car_num, inout = record.split(" ")
        if inout == "IN":
            data_inout[car_num] = str_to_min(time)
        else:
            t = str_to_min(time) - data_inout.pop(car_num)
            data_time[car_num] += t
    
    # 남아있는 차 출차
    for key, val in data_inout.items():
        data_time[key] += 1439 - val

    # 정산
    for key, val in data_time.items():
        if val <= basic_m: # 기본요금
            answer.append([key, basic_w])
        else: #추가요금
            won = basic_w + ceil((val-basic_m)/unit_m) * unit_w
            answer.append([key, won])

    answer.sort(key= lambda x: x[0])
    return [ i[1] for i in answer]

print(solution([180, 5000, 10, 600],	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

# 기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
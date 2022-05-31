# set에 소수 저장
# n 자리수 모두 검색
# 소수라면 오른편 절단 소수인지 검색
# 출력

set_of_decimal = {2}
n = int(input())                    # 자리수 입력
start, end = 10**(n-1), 10**n

def discrim_decimal(i):
    for j in set_of_decimal:
        if not i % j:
            break
    else:
        set_of_decimal.add(i)
        return True
    return False

def check_right(i):
    while i > 0 and i in set_of_decimal:
        i = i // 10
    if i == 0:
        return True
    return False


for i in range(3, start):           # start 이전 소수
    discrim_decimal(i)

for i in range(start, end):
    if discrim_decimal(i):
        if check_right(i):
            print(i)
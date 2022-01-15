from math import sqrt
# 10진수 3~9진수로 변환
def convert(n, base):
    T = "0123456789"
    q, r = divmod(n, base)
    return convert(q, base) + T[r] if q else T[r]

# 소수 판별 (효율성 위해 제곱근까지만)
def prime_check(n):
    if n == 1:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1


def solution(n, k):
    answer = 0
    # 진수 변환
    if k < 10:
        n = convert(n, k)
    else:
        n = str(n)
    # 소수 판별 분리
    prime_list = n.split("0")
    # 소수 판별
    for prime in prime_list:
        if prime != '' and prime_check(int(prime)):
            answer += 1

    return answer

print(solution(437674,	3))
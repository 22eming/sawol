from math import sqrt
def convert(n, base):
    T = "0123456789"
    q, r = divmod(n, base)
    return convert(q, base) + T[r] if q else T[r]

def prime_check(n):
    if n == 1:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    if k < 10:
        n = convert(n, k)
    else:
        n = str(n)
    prime_list = n.split("0")
    print(prime_list)
    for prime in prime_list:
        if prime != '' and prime_check(int(prime)):
            answer += 1

    return answer

print(solution(437674,	3))
print(solution(110011,	10))
print(solution(8,	4))
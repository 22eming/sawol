from math import factorial
def solution(n, k):
    answer = []
    res = [i for i in range(1,n+1)]
    for i in range(1, n):
        x,k = divmod(k, factorial(n-i))
        if k == 0:
            answer.append(res.pop(x-1))
            continue
        if i == n-1:
            answer.append(res.pop(k))
            answer.append(res[0])
            break
        answer.append(res.pop(x))
    if res != []:
        answer.append(res[0])

    return answer


print(solution(4,12))

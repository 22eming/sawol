from math import ceil
def solution(n, stations, w):
    answer = 0
    s = 1
    for i in stations:
        answer += ceil((i - s - w)/(2*w+1))
        s = i + w + 1

    answer += ceil((n - s+1)/(2*w+1))
    return answer
print(solution(16,	[9],	2))

# 금 akg 은 bkg
# i 도시에 g[i]금 s[i]은 트럭한대
# 편도 이동 t[i] 시간
# 최대 w[i]kg 운반 가능

def solution(a, b, g, s, w, t):
    answer = 10e5 * 4 * 10e9
    start, end = 0, max(t) * max(a, b)*4
    while start <= end:
        mid = (end + start) // 2
        gold, silver, total = 0, 0, 0
        for now in zip(g, s, w, t):
            cnt = ((mid // now[3])+1)//2
            gold += min(now[2]*cnt, now[0])
            silver += min(now[2]*cnt, now[1])
            total += min(now[2]*cnt, now[1]+now[0])

        if (gold >= a and silver >= b and total >= a+b):
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer


print(solution(10,	10,	[100], [100], [7], [10]))

def s(stones, idx, k):
    m = max(stones[idx:idx+k])
    index_m = stones[idx:idx+k].index(m) + idx
    return m, index_m

def solution(stones, k):
    m, index_m = s(stones, 0, k)
    answer = m

    for idx, i in enumerate(stones[k:]):
        if stones[i] > m:
            m = i
            index_m = idx+k
        elif idx == index_m:
            m, index_m = s(stones, idx+1, k)
            answer = min(answer, m)

    return answer



print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	,3))
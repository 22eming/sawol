from collections import Counter


def solution(land, P, Q):
    answer = float('inf')
    land = sum(land, [])
    count_land = Counter(land)
    total, minus = sum(land), 0
    col, m_col = len(land), 0
    for i in sorted(count_land.keys()):
        # 삭제 : 남은 블록 - (남은 기둥 * 현재 기둥높이)
        # 추가 : (삭제된 기둥 * 현재 기둥 높이) - 삭제된 블록 개수
        d = total-minus - ((col-m_col) * i)
        a = (m_col * i) - minus
        answer = min(answer, a*P + d*Q)
        
        minus += count_land[i] * i
        m_col += count_land[i]

    return answer


print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]],5,3))
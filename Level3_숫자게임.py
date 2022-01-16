"""
먼저 모든 사원이 무작위로 자연수를 하나씩 부여받습니다.
각 사원은 딱 한 번씩 경기를 합니다.
각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개합니다. 그때 숫자가 큰 쪽이 승리하게 되고, 
    승리한 사원이 속한 팀은 승점을 1점 얻게 됩니다.
만약 숫자가 같다면 누구도 승점을 얻지 않습니다.
"""
import bisect
def solution(A, B):
    answer = 0
    B_rank = {}
    for i in B: # B의 숫자 보유현황
        if B_rank.get(i) == None:
            B_rank[i] = 1
        else:
            B_rank[i] += 1

    rank = sorted(B_rank.keys())

    for i in A:
        index = bisect.bisect_right(rank, i)    # 승리 할 수 있는 최소값 인덱스
        if index == len(rank):  # 이길 수 없을때 
            continue
        else:
            B_rank[rank[index]] -= 1
            answer += 1
            if B_rank[rank[index]] == 0: # 숫자를 다 사용하면 지우기
                del rank[index]
    
    return answer

print(solution([5,1,3,7],	[2,2,6,8]))


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(B)):
        if A[j] < B[i]:
            answer += 1
            j += 1

    return answer
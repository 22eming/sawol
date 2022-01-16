from itertools import permutations


def solution(n, weak, dist):
    len_weak = len(weak)
    # 배열을 *2로 만들어서 연결리스트처럼 사용
    for i in range(len_weak):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    # 첫 시작 위치 변경
    for i in range(len_weak):
        # 탐색할 위치
        search_point = weak[i:i+len_weak]
        # 탐색할 친구들 순서
        friendes = permutations(dist)

        # 친구 투입 순서 모두 대입
        for friend in friendes:
            friend_idx, friend_cnt = 0, 1
            # 친구의 최대 탐색 거리
            friend_power = search_point[0] + friend[friend_idx]
            # weak 전체 탐색
            for idx in range(len_weak):
                # 친구의 최대 탐색 거리 초과시
                if friend_power < search_point[idx]:
                    friend_cnt += 1
                    # 더 탐색할 친구가 없을 시
                    if len(friend) < friend_cnt:
                        break
                    friend_idx += 1
                    # 최대 탐색 거리 초기화
                    friend_power = search_point[idx] + friend[friend_idx]
            answer = min(answer, friend_cnt)

    if answer > len(dist):
        return -1

    return answer


print(solution(200,	[0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))

from collections import defaultdict
import heapq
INF = float('inf')

def is_state(cur_start, next_start, trap_state, trap ):
    _cur, _next = False, False
    if cur_start in trap:
        _cur = trap_state & (1 << trap[cur_start]) > 0
    if next_start in trap:
        _next = trap_state & (1 << trap[next_start]) > 0
    
    # 함정 두개의 상태가 같으면 원상태
    return _cur != _next 

def state_change(next_start, cur_state, trap):
    if next_start in trap:
        return cur_state ^ ( 1 << trap[next_start])
    return cur_state

def solution(n, start, end, roads, traps):
    answer = INF
    visited = [ [False]*(n+1) for _ in range(2**len(traps)) ]

    # 그래프 생성   
    graph = defaultdict(list) 
    for _start, _end, _cost in roads:
        graph[_start].append( [_cost, _end, False] ) # 정방향
        graph[_end].append( [_cost, _start, True] ) # 역방향

    # 트랩
    trap = {t:i for i, t in enumerate(traps)}

    # 초기화
    heap = []
    heapq.heappush(heap, [0, start, 0])


    while heap:
        cur_cost, cur_start, cur_state = heapq.heappop(heap)
        if cur_start == end:
            return cur_cost
        if visited[cur_state][cur_start]:
            continue
        visited[cur_state][cur_start] = True

        for next_cost, next_start, trap_state in graph[cur_start]:
            # 순방향 역방향
            if trap_state != is_state(cur_start, next_start, cur_state, trap):
                continue
            
            next_state = state_change(next_start, cur_state, trap)
            next_cost = cur_cost + next_cost
            heapq.heappush(heap, [next_cost, next_start, next_state])

    return answer


print(solution(4,	1,	4,	[[1, 2, 1], [3, 2, 1], [2, 4, 1]],	[2, 3]))
# trap = {2: [[1,3], [4]]}
# visited_trap = {2:0, 3:1}
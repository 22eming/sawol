from collections import defaultdict, deque

# 락이 풀렸을때 stack에 넣는다.

def dfs(cave, after):
    stack = deque([0])
    stp = {}
    visited = set()
    while stack:
        s = stack.pop()
        if s in after and after[s] not in visited:
            stp[after[s]] = s
            del after[s]
            continue
        if s in stp:
            stack.append(stp[s])
            del stp[s]
        visited.add(s)
        for i in cave[s]:
            if i not in visited:
                stack.append(i)
    return stp == {}



def solution(n, path, order):
    cave = defaultdict(list)
    # 경로
    for p, c in path:
        cave[p].append(c)
        cave[c].append(p)
    
    # 제한
    after = {}
    for p,c in order:
        after[c] = p
    
    return dfs(cave, after)


print(solution(9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[8,5],[6,7],[4,1]]))
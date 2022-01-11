def bfs(queen, x, n):
    cnt = 0
    if x == n:
        return 1
    
    for y in range(n):
        queen[x] = y
        for xx in range(x):
            if y in queen[:x]:
                break
            if abs(queen[x]- queen[xx]) == x - xx:
                break
        else:
            cnt += bfs(queen, x+1, n)
    return cnt
        

def solution(n):
    queen = [0]*n
    return bfs(queen, 0, n)


print(solution(6))
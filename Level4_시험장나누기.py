import sys
sys.setrecursionlimit(10001)
tree = {}
cnt = 0
people = []

def dfs(root, lim):
    global cnt
    _left, _right = tree[root]
    left_val, right_val = 0, 0
    if _left != -1:
        left_val = dfs(_left, lim)
    if _right != -1:
        right_val = dfs(_right, lim)

    cur = people[root]
    # 둘 다 합쳐도 lim 이하
    if cur + left_val + right_val <= lim:
        return cur + left_val + right_val
    # 최소값 합치면 lim 이하
    elif cur + min(left_val, right_val) <= lim:
        cnt += 1
        return cur + min(left_val, right_val)
    # lim 이상
    else:
        cnt += 2
        return cur


def solution(k, num, links):
    global cnt, people, tree
    p = [False] * (len(num)+1)

    for idx, link in enumerate(links):
        _left, _right = link
        tree[idx] = (_left, _right)
        p[_left] = True
        p[_right] = True
    
    people = num
    root = p.index(False)

    _sum = sum(num)
    s = _sum // k
    e = _sum
    while s < e:
        mid = (s + e) // 2
        dfs(root, mid)
        if  cnt < k:
            e = mid
        else:
            s = mid + 1
        cnt = 0
    return s

# 트리의 왼쪽 합 오른쪽 합 정리
print(solution(3,	[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],	[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))

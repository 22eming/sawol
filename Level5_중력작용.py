from collections import defaultdict, deque
import sys
sys.setrecursionlimit(100001)

q1, parent, val = [], [], []
tree = defaultdict(list)

def mk_tree(temp):
    que = deque([1])
    visited = {1}

    while que:
        node = que.popleft()
        for i in temp[node]:
            if i not in visited:
                visited.add(i)
                tree[node].append(i)
                que.append(i)
                parent[i] = node


def mk_quer_one(root):
    for i in tree[root]:
        q1[root] += mk_quer_one(i)
    q1[root] += val[root]
    return q1[root]

def ch_quer_two(node):
    diff = 0
    while parent[node]:
        diff += val[parent[node]] - val[node]
        q1[node] += diff
        val[node] = val[parent[node]]
        node = parent[node]
    q1[1] += diff

def solution(values, edges, queries):
    global q1, parent, val
    answer = []
    val = [0] + values
    q1 = [0] * len(val)
    parent = [0] * len(val)
    
    temp = defaultdict(list)

    for p, c in edges:
        temp[p].append(c)
        temp[c].append(p)

    mk_tree(temp)
    mk_quer_one(1)

    for u, w in queries:
        if w == -1:
            answer.append(q1[u])
        else:
            ch_quer_two(u)
            q1[1] += w - val[1]
            val[1] = w

    return answer

v = [1,10,100,1000,10000]
e = [[1,2],[1,3],[2,4],[2,5]]
q = [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]

v = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
e = [[10, 11], [13, 11], [12, 10], [10, 9], [8, 9], [1, 2], [2, 4], [2, 3], [5, 3], [6, 5], [5, 8], [7, 5]]
q = [[13, 8192], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [6, -1], [7, -1], [8, -1], [9, -1], [10, -1], [11, -1], [12, -1], [13, -1]]
print(solution(v, e, q))
# queries의 1 값이 -1이면 1번 쿼리

# 1번 쿼리
    # u번 노드와 자식 노드의 합
# 2번 쿼리
    # 부모노드의 값으로 교체 루트 노드는 w값으로 교체

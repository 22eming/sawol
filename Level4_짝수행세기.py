def solution(a):
    answer = -1
    # 열 별 개수
    row = [0] * len(a[0])
    for i in range(len(row)):
        for j in range(len(a)):
            if a[j][i]:
                row[i] += 1

    print(row)

    return False

print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
print(solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]))


from itertools import combinations

print(len(list(combinations([1,2,3,4], 2))))

# 4행 4쌍
# 4행 3쌍

print(6*4)
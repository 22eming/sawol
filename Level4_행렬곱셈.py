from collections import defaultdict

def matrix_multi(sorted_mid, matrix):
    for mid, cnt in sorted_mid:
        for _ in range(cnt):
            # cnt가 1이 아닐때 col, row 값 골라야함
            pass

def solution(matrix_sizes):
    answer = float('inf')
    _matrix = defaultdict(list)
    _mid = defaultdict(int)
    wait_col, wait_row = set(), set()
    for col, row in matrix_sizes:
        # col, row 구별 필요
        _matrix[col].append(row)
        _matrix[row].append(col)

        if col in wait_col:
            _mid[col] += 1
        else:
            wait_row.add(col)

        if row in wait_row:
            _mid[row] += 1
        else:
            wait_col.add(row)
    
    print(sorted(_mid.items(), reverse=True ))
    print(_matrix.items())
    return answer

# 중간값이 큰 값 먼저 계산

print(solution([ [10,3], [10,5], [4, 10], [7, 10], [4, 7] ]))

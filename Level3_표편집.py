def solution(n, k, cmd):
    # 링크리스트로 구현
    # 삭제시 링크리스트 다음 리스트로 연결
    # 연결시 링크리스트 다시 연결
    node = {0: [n-1, 1]}
    for i in range(1, n):
        if i != n-1:
            node[i] = [i-1, i+1]
        else:
            node[i] = [i-1, 0]

    del_l = []
    for c in cmd:
        command = c[0]
        if len(c) > 1:
            command, x = c.split(" ")
            # U X : x칸 위에 행 선택
            if command == "U":
                cnt = int(x)
                for _ in range(cnt):
                    k = node[k][0]
            # D X : x칸 아래있는 행 선택
            elif command == "D":
                cnt = int(x)
                for _ in range(cnt):
                    k = node[k][1]
        # C : 현재 행 삭제 아래 행 선택 if 마지막행 바로 윗 행 선택
        elif command == "C":
            node[node[k][0]][1] = node[k][1]
            node[node[k][1]][0] = node[k][0]
            del_l.append([k, node[k]])
            tmp = node[k]
            del node[k]

            if tmp[1] < k:
                k = tmp[0]
            else:
                k = tmp[1]
        # Z : 최근 삭제 행 복구 but 현재 선택된 행은 바뀌지 않음
        elif command == "Z":
            idx, link = del_l.pop()
            node[idx] = [link[0], link[1]]
            node[link[0]][1] = idx
            node[link[1]][0] = idx

    answer = ''
    for i in range(n):
        if node.get(i) == None:
            answer += 'X'
        else:
            answer += 'O'
    return answer


print(solution(8,	2,	["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))

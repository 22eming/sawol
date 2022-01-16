def solution(s):
    answer = []
    for i in s:
        stack = []
        # 110 제거
        for val in i:
            if val == "0" and stack[-2:] == ["1", "1"]:
                del stack[-2:]
            else:
                stack.append(val)
        # 제거된 110 수
        cnt = (len(i) - len(stack))//3
        # 0이 없을 시 기본 index
        index = -1
        # rfind(0)
        for s in range(len(stack)-1, -1, -1):
            if stack[s] == '0':
                index = s
                break

        answer.append("".join(stack[:index+1] + ["110"]*cnt + stack[index+1:]))

    return answer


print(solution(["1110", "100111100", "0111111010"]))

def solution(s):
    answer = len(s)
    for cut in range(1, len(s)//2 + 1):
        cnt = 1
        temp = s[:cut]
        result = 0
        for x in range(cut, len(s), cut):
            if s[x:x+cut] == temp:
                cnt += 1
            else:
                result += cut if cnt == 1 else cut+len(str(cnt))
                temp = s[x:x+cut]
                cnt = 1
        result += len(temp) if cnt == 1 else cut+len(str(cnt))
        answer = min(answer, result)
            
    return answer
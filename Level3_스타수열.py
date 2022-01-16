from collections import Counter


def solution(a):
    common = Counter(a).most_common()
    answer = 0
    for c in common:
        if c[1]*2 <= answer*2:
            break
        cnt = 0
        l = [0]*len(a)
        for i in range(len(a)):
            if a[i] == c[0]:
                l[i] = 1
                if i == len(l)-1:
                    if l[i-1] != 1:
                        cnt += 1
                else:
                    if a[i+1] == c[0]:
                        l[i+1] = 1
                    if i > 0:
                        if l[i-1] != 1:
                            l[i-1] = 1
                            cnt += 1
                        elif l[i+1] != 1:
                            l[i+1] = 1
                            cnt += 1
                    else:
                        if l[i+1] != 1:
                            l[i+1] = 1
                            cnt += 1
        answer = max(answer, cnt)
    return answer*2


answer = [4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3]
print(solution(answer))

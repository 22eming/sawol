from math import ceil
def solution(N, number):
    if N==number:
        return 1
    ss = [[int(N)]]
    for i in range(2,9):#i개로 만들 수 있는 숫자들i:2~8
        a=[]
        b=int(str(N)*i)
        a.append(b)
        for p in range(i-2,ceil(i//2)-2,-1):
            for j in ss[p]: #p : 0~7
                for k in ss[i-p-2]:
                    a.append(int(j)+int(k))
                    a.append(int(j)-int(k))
                    a.append(int(j)*int(k))
                    a.append(int(k)-int(j))
                    if int(k)!=0:
                        a.append(int(j)//int(k))
                    if int(j)!=0:
                        a.append(int(k)//int(j))
        ss.append(list(set(a)))
        if number in a:
            return i

    return -1

print(solution(1,1121))
# 2
# 1   1
# 3
# 2   1
# 4
# 3   1
# 2   2
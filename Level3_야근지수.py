def solution(n, works):
    works.sort(reverse= True)
    res = 0
    for i in range(1,len(works)):
        a = works[i-1]-works[i]
        if a > 0:
            res += a*len(works[:i])
        if res == n:
            return (works[i]**2 * (i+1)) + sum([j**2 for j in works[i+1:]])
        elif res > n:
            x,y = divmod(res - n, i)
            # x만큼 더하고 y갯수만큼 1더함
            return ((works[i]+x)**2 * (i-y)) + ((works[i]+x+1)**2 * y) + sum([j**2 for j in works[i:]])
    
    #else : work[-1] 값에서 빼야함
    x,y = divmod(n-res, i+1)
    a = works[-1]-x-1 ; b = works[-1]-x
    if b < 0: a = 0; b = 0
    elif a < 0: a = 0
    return ((b)**2 * (i+1-y)) + ((a)**2 * (y))

print(solution(5,[1,1]))

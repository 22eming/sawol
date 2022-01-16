def solution(n, money):
    arr = [1] + [0]*n
    for c in money:
        for i in range(c, n+1):
            arr[i] += arr[i-c]
    return arr.pop()
    
print(solution(10,[1,2,5]))

start, end = map(int, input().split())

def mul(n):
    res = 1
    while n > 0:
        res *= n%10
        n = n // 10
    return res

print(sum([mul(i) for i in range(start, end+1)]))


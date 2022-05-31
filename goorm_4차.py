def input_user():
	n = int(input())
	arr = list(map(lambda x: x.split('+'), input().split() )) # 식 분리 -> 복소수 분리
	return arr

def solution(arr):
	a, b = int(arr[0][0]), int(arr[0][1][:-1])
	for c, d in arr[1:]:  # 이항식 계산
		c, d = int(c), int(d[:-1])
		a, b = a*c - b*d, a*d + b*c						# ac - bd + (ad + bc)i
		
	a, b = map(lambda x: x%10007 if x >= 0 else x%-10007, [a,b])
	print(f"{a}+{b}i")


solution(input_user())
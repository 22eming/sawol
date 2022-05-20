def total_mul(n):
	res = 1
	for i in str(n):
		res *= int(i)
	return res

user_input = int(input())
max_num = total_mul(user_input)

for n in range(1, len(str(user_input))):
	user_input = user_input // 10 - 1
	if user_input == -1:
		user_input = 0
	max_num = max(max_num, total_mul( user_input * (10**n) + int("9"*n) ))

print(max_num)
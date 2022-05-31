# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
life, wonder = map(int, input().split()) #살아온 날짜 , 궁금한 날짜
history = list(map(int, input().split()))

n = 0 
history_sum = [0]
for i in history:
	n += i
	history_sum.append(n)

for _ in range(wonder):
	a, b = map(int, input().split())
	print( "{:+d}".format(history_sum[b] - history_sum[a-1] ))


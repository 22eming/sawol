n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
empty_board = [[0]*m for _ in range(n)]

def fill_line(em_board, loc, d):
	y, x = loc
	if d == 1: # 가로
		for x in range(len(em_board[0])):
			em_board[y][x] = 1
	elif d == 2:
		for y in range(len(em_board)):
			em_board[y][x] = 1
	return em_board

for y in range(n):
	for x in range(m):
		if board[y][x] == 1: # 가로
			empty_board = fill_line(empty_board, [y,x], 1)
			
		elif board[y][x] == 2: # 세로
			empty_board = fill_line(empty_board, [y,x], 2)
			
		elif board[y][x] == 3: # 십자
			empty_board = fill_line(empty_board, [y,x], 1)
			empty_board = fill_line(empty_board, [y,x], 2)

print(sum([1 for y in range(n) for x in range(m) if empty_board[y][x] == 0 ]))


		
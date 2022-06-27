from collections import deque

n, k = map(int, input().split())
user_data = {i:deque() for i in range(1, n+1)}

log = []

for _ in range(k):
	user_id, msg = input().split()
	user_id = int(user_id)
	
	if msg.isnumeric():
		user_data[user_id][int(msg)-1] = 'deleted'
	else:
		log.append(user_id)
		user_data[user_id].append(msg) 


for i in log:
	print(f"{i} {user_data[i].popleft()}")


"""

"""
import sys
sys.setrecursionlimit(200001)

def recur_room(room, full_room):
    if room not in full_room:
        full_room[room] = room+1
        return room
    
    empty = recur_room(full_room[room], full_room)
    full_room[room] = empty+1
    return empty

def solution(k, room_number):
    full_room = {}
    for number in room_number: 
        recur_room(number, full_room)
    return list(full_room.keys())
 

print(solution(10,	[1,3,4,1,3,1]))
# 방이 비어있으면 바로 배정
# 차있으면 방번호 보다 크며 비어있는 방 중에 번호가 가장 작은 방
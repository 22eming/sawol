from collections import defaultdict

x, y = 1, 1                                                     # 1,1 시작, end_x, end_y 끝
end_y, end_x, k = map(int, input().split())
# 어째서 N이 -? E가 -?
move_robot = {'N':[0,-1], 'W':[1,0], 'S':[0,1], 'E':[-1,0]}     # [x,y] 로봇 이동 방향 설정
visited = defaultdict(int)                                      # 방문 내역
visited['1_1'] += 1

for d in list(input()):                                         # 리스트로 하나씩 읽어온다
    dx, dy = move_robot[d]                                      # 이동 받아옴
    x += dx
    y += dy

    if x < 1 or x > end_x:                                      # 위치 조절
        x = min(max(1,x), end_x)
    if y < 1 or y > end_y:
        y = min(max(1,y), end_y)

    visited[f"{x}_{y}"] += 1                                    # 방문 카운트

print(max(visited.values()))                                    # 최대값 가져옴
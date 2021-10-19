# from collections import deque
# order : 미생물이 있는 좌표들. 이것을 pop해서 좌표접근 ->set으로 합쳐지는 중복좌표 제거
# board : (생물수,방향)
# direction : (생물합,최대군집의 생물 수,최다군집방향)

n, m, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
direction = [[0 for _ in range(n)] for _ in range(n)]
tmp_direction = [[0 for _ in range(n)] for _ in range(n)]
d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # [0 상 하 좌 우]
order = set()
result = 0

for _ in range(k):
    x, y, num, dd = map(int, input().split())
    board[x][y] = (num, dd)
    order.add((x, y))

for i in range(m):  # 총 실행시간
    tmp_board = [[0 for _ in range(n)] for _ in range(n)]
    tmp_order = set() #미생물이 존재하는 위치들의 배열(set)
    length = len(order)
    for _ in range(length):
        x, y = order.pop()

        cur_value, dir = board[x][y]
        dx, dy = d[dir]
        X, Y = x + dx, y + dy
        if X == 0 or X == (n - 1) or Y == 0 or Y == (n - 1):  # 끝으로 갔다면
            if dir == 1: new_dir = 2 #방향 반대로 바꾸기 (식으로 표현을 못하겠어서 일일히 만듬)
            elif dir == 2: new_dir = 1
            elif dir == 3: new_dir = 4
            else: new_dir = 3
            tmp_order.add((X, Y))
            tmp_direction[X][Y] = (cur_value // 2, cur_value // 2, new_dir) # direction : (생물합,최대군집의 생물 수,최다군집방향)
            tmp_board[X][Y] = (cur_value // 2, new_dir)

        else:  # 이미 위 if문으로 끝을 넘어갈 일은 없음
            tmp_order.add((X, Y))
            if tmp_direction[X][Y] != 0:  # 이미 하나가 들어가있다면
                sum_num, max_val, max_dir = tmp_direction[X][Y]
                if cur_value > max_val:  # 더 큰 군집이라면 그 방향을 넣음
                    tmp_direction[X][Y] = (sum_num + cur_value, cur_value, dir)
                    tmp_board[X][Y] = (sum_num + cur_value, dir)

                else:  # 작은군집이라면 합에만 추가
                    tmp_direction[X][Y] = (sum_num + cur_value, max_val, max_dir)
                    tmp_board[X][Y] = (sum_num + cur_value, max_dir)

            else:  # 처음 넣는 경우라면(만나지않았다면)
                tmp_direction[X][Y] = (cur_value, cur_value, dir)
                tmp_board[X][Y] = board[x][y]

    # 사이클 끝, 다시 초기화
    board = [item[:] for item in tmp_board] #새로운 정보로 변경
    tmp_direction = [[0 for _ in range(n)] for _ in range(n)] #direction 0으로 초기화
    order = tmp_order #생물 위치들 변경

for i, j in order:
    result += board[i][j][0]
print(result)

"""
7 2 9
1 1 7 1
2 1 7 1
5 1 5 4
3 2 8 4
4 3 14 1
3 4 3 3
1 5 8 2
3 5 100 1
5 5 1 1
"""

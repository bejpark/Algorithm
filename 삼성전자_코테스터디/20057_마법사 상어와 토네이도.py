#1 파이썬 -1인덱스 접근가능, 예외처리로 안되고 직접 범위지정해야했음
#2 방향별로 돌려주는 문제, delft만 구현하고 나머지는 관계식으로
#3 모래는 퍼센트 후 소수점을 버리기때문에 알파자리에 100-나머지퍼센트를 하면 안되고 전체모래-빠진모래를 넣어야함

def storm(xx, yy, direction):
    global N, result, board

    sand = board[xx][yy]
    sum_sand = 0
    for dx, dy, percent in dleft:
        if direction == 1:  # 왼쪽
            X, Y = xx + dx, yy + dy
        elif direction == 2:  # 아래쪽
            X, Y = xx - dy, yy + dx
        elif direction == 3:  # 오른쪽
            X, Y = xx + dx, yy - dy
        elif direction == 4:  # 위쪽
            X, Y = xx + dy, yy + dx

        if 0 <= X < N and 0 <= Y < N:  # 각 퍼센트별 모래 이동
            s = sand * percent // 100
            sum_sand += s
            board[X][Y] += s
        else:  # 나간 경우
            s = sand * percent // 100
            result += s
            sum_sand += s

    board[xx][yy] = 0
    #파이썬은 배열에 -1인덱스도 넣을수 있기 때문에 except문을 써도 -1은 그대로 적용됨
    if direction == 1:  # 왼쪽
        if yy>0:
            board[xx][yy - 1] += (sand - sum_sand)
        else:
            result += (sand - sum_sand)
    elif direction == 2:  # 아래쪽
        if xx<N-1:
            board[xx + 1][yy] += (sand - sum_sand)
        else:
            result += (sand - sum_sand)
    elif direction == 3:  # 오른족
        if yy<N-1:
            board[xx][yy + 1] += (sand - sum_sand)
        else:
            result += (sand - sum_sand)
    elif direction == 4:  # 위쪽
        if xx>0:
            board[xx - 1][yy] += (sand - sum_sand)
        else:
            result += (sand - sum_sand)



N = int(input())
board = []
result = 0
dleft = [(-2, 0, 2), (-1, 0, 7), (1, 0, 7), (2, 0, 2), (-1, -1, 10), (1, -1, 10), (1, 1, 1), (-1, 1, 1),
         (0, -2, 5)]  # x,y,모래 퍼센트

for _ in range(N):
    board.append(list(map(int, input().split())))

x = N // 2
y = N // 2
k = 1
direction = 1
while True:  # 토네이도 도는곳
    if x == 0:
        for i in range(1, k):
            storm(x, y - i, 1)
        break
    if direction == 1:
        for i in range(1, k + 1):  # 왼
            storm(x, y - i, 1)
        y = y - k
        for i in range(1, k + 1):  # 아래
            storm(x + i, y, 2)
        x = x + k
        k += 1
        direction = 0
    else:
        for i in range(1, k + 1):  # 오른
            storm(x, y + i, 3)
        y = y + k
        for i in range(1, k + 1):  # 위
            storm(x - i, y, 4)
        x = x - k
        k += 1
        direction = 1

print(result)


# 아래, 우측 보드를 각각 구현하지 않고 빨간색 영역을 회전시켜 같은 보드에 넣는 방식으로 구현

def insertBlock(type, x, y):
    if type == 1:
        redBoard[x][y] = 1
    elif type == 2:
        redBoard[x][y] = 1
        redBoard[x][y + 1] = 1
    else:
        redBoard[x][y] = 1
        redBoard[x + 1][y] = 1


def moveBlock(board):
    global redBoard, tmp
    tmp = [items[:] for items in redBoard]
    # 내린걸 red에 바로 저장하면 이후 rotate할 때 문제 발생 임시배열에 넣고 써야함
    while tmp[3] == [0, 0, 0, 0]:  # red 상에서 아래로 내리기
        tmp[3] = tmp[2]
        tmp[2] = tmp[1]
        tmp[1] = tmp[0]
        tmp[0] = [0, 0, 0, 0]

    i = 0 #board의 맨 위에서부터 내려오면서 놓을자리 찾기
    while True:
        flag = False #겹치면 True
        for j in range(4):
            if board[i][j] == 1 and tmp[3][j] == 1:  # 겹치면(해당자리 둘 다 1인 경우)
                #ㅣ모양은 어차피 . 모양으로 생각해도됨
                flag = True
                break

        if flag or i == 5:  # 겹치거나 맨 아래까지 갔다면
            if i == 5 and not flag:  # 겹치지 않고 맨 아래까지 간 경우
                pass
            else:
                # 겹치는 경우 바로 위 행에 넣어준다.
                i -= 1
            for xx in range(2): #range(2)인 이유는 ㅣ 모양때문..
                for yy in range(4):
                    if tmp[xx + 2][yy] == 1:
                        board[i + xx - 1][yy] = 1
            break

        i += 1


def clearBlock(board):
    global score

    for i in range(2, 6):  # 찬 블록 먼저 삭제
        if board[i] == [1, 1, 1, 1]:
            board[1:i + 1] = board[0:i]
            board[0] = [0, 0, 0, 0]
            score += 1

    if board[0] != [0, 0, 0, 0]:  # 맨 윗칸에 채워진게 있을 때 2칸 밀음
        board[2:] = board[0:4]
        board[0] = [0, 0, 0, 0]
        board[1] = [0, 0, 0, 0]
    elif board[1] != [0, 0, 0, 0]:  # 1행에만 채워진게 있을 때 1칸 밀음
        board[2:] = board[1:5]
        board[1] = [0, 0, 0, 0]


def rotate90():
    global redBoard, tmp
    tmp = [items[:] for items in redBoard]

    for i in range(4):
        for j in range(4):
            redBoard[j][3 - i] = tmp[i][j]


n = int(input())
redBoard = [[0 for _ in range(4)] for _ in range(4)]
blueBoard = [[0 for _ in range(4)] for _ in range(6)]
greenBoard = [[0 for _ in range(4)] for _ in range(6)]
tmp = [] #임시로 돌려쓸 배열
score = 0
count = 0  # 블록이 있는 칸 수

for _ in range(n):
    t, x, y = map(int, input().split())
    #red에 블록채움 -> green에 적용,점수적용 -> 90도 돌림 -> blue에 적용,점수적용
    insertBlock(t, x, y)
    moveBlock(greenBoard)
    clearBlock(greenBoard)
    rotate90()
    moveBlock(blueBoard)
    clearBlock(blueBoard)

    redBoard = [[0 for _ in range(4)] for _ in range(4)]  # 블럭 사용 후 초기화

for i in range(2, 6):
    for j in range(4):
        if blueBoard[i][j] == 1:
            count += 1
        if greenBoard[i][j] == 1:
            count += 1

print(score)
print(count)

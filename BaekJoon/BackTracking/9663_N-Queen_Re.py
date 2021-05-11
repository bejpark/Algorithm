"""
#9663
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

#출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
"""
"""
#1
import sys
n = int(sys.stdin.readline())
result = 0

def check(current,current_col):
    current_row = len(current)
    for row in range(current_row):
        if current[row] == current_col or abs(current[row]-current_col)==current_row-row:
            return False
    return True


def dfs(n, current_row, current):
    global result
    if current_row == n:
        result+=1
        return
    for i in range(n):
        if check(current, i):
            current.append(i)
            dfs(n,current_row+1,current)
            current.pop()
dfs(n,0,[])
print(result)
"""
#2
n = int(input())
row = [0]*n
result = 0
def check(a):
    for i in range(a):
        if row[a]==row[i]:
            return False
        if abs(row[a]-row[i])==a-i:
            return False
    return True

def dfs(a):
    global result
    if a == n:
        result+=1
    else:
        for i in range(n):
            row[a]=i
            if check(a):
                dfs(a+1)
dfs(0)
print(result)

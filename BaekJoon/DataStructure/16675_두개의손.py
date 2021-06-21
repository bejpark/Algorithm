"""
#16675
민성이와 태경이는 고려대학교에서 알아주는 가위바위보의 최고수들이다. 이들은 기존의 가위바위보에 질린 나머지, 2개의 손을 모두 이용하여 가위바위보를 즐기는 경지에 이르렀다.

먼저, 둘이 동시에 “가위, 바위, 보”를 외치며 두 개의 손을 각각 가위, 바위, 보 중 하나로 설정하여 공개한다.
그 자리에서 서로 3초간 호흡을 가다듬은 후, 동시에 왼손을 낼지 오른손을 낼지를 결정한다.
민성이와 태경이는 최고수들끼리의 대결이라는 압박감에 의해 가끔 판단력이 흐려질 때가 있어서, 실수로 왼손과 오른손에 같은 동작을 취할 수도 있다.

당신은 민성이와 태경이의 왼손과 오른손의 상태가 주어졌을 때, 민성이 또는 태경이가 적절히 왼손 또는 오른손을 선택하여 가위바위보에서 무조건 이기는 방법이 있는지 없는지를 알려고 한다.

#입력
첫 번째 줄에 차례로 ML, MR, TL, TR이 공백으로 구분되어 주어진다. 
차례대로 민성이의 왼손과 오른손, 태경이의 왼손과 오른손의 상태를 나타낸다.

위 4개의 값들은 “S”, “R”, “P” 중 하나이며, 각각 가위, 바위, 보를 의미한다.

#출력
첫 번째 줄에 민성이가 무조건 이길 수 있다면 “MS”, 태경이가 무조건 이길 수 있다면 “TK”, 누가 이길 지 확답할 수 없다면 “?”를 쌍따옴표를 제외하고 출력한다.

가위바위보에서 가위는 보를 이기고, 바위는 가위를 이기며, 보는 바위를 이긴다. 같은 손동작끼리는 승부가 나지 않는다 (비긴다).
"""

"""
arr = list(input().split())

def round(a,b): #a가 이기면 1, 비기면 0, 지면 -1
    if a == 'R':
        if b == 'R':
            return 0
        elif b == 'S':
            return 1
        else:
            return -1
    elif a == 'S':
        if b == 'R':
            return -1
        elif b == 'S':
            return 0
        else:
            return 1
    else: #P
        if b == 'R':
            return 1
        elif b == 'S':
            return -1
        else:
            return 0
if arr[0] == arr[1] and arr[2] != arr[3]:
    match1 = round(arr[0],arr[2])
    match2 = round(arr[0],arr[3])
    if match1 == -1 or match2 == -1:
        print('TK')
    else:
        print('?')
elif arr[2] == arr[3] and arr[0] != arr[1]:
    match1 = round(arr[2],arr[0])
    match2 = round(arr[2],arr[1])
    if match1 == -1 or match2 == -1:
        print('MS')
    else:
        print('?')
elif arr[0]==arr[1] and arr[2]==arr[3]:
    match = round(arr[0],arr[2])
    if match==1:
        print('MS')
    elif match==-1:
        print('TK')
    else:
        print('?')
else:
    print('?')

"""
#2
ML, MR, TL, TR = ('SPR'.index(i) for i in input().split()) #SPR에 대해 012 부여

if ML == MR and (ML+2)%3 in (TL,TR): #+2 %3 이 이기는 인덱스
    print('TK')
elif TL == TR and (TL+2)%3 in (ML,MR):
    print('MS')
else:
    print('?')
def solution(numbers, target):
    global answer
    answer=0
    dfs(numbers,0,0,target)
    return answer


def dfs(numbers,result,idx,target):
    global answer
    if idx==len(numbers):
        if result==target:
            answer+=1
        return
    dfs(numbers,result+numbers[idx],idx+1,target)
    dfs(numbers,result-numbers[idx],idx+1,target)
